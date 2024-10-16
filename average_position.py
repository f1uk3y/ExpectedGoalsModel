import csv
import os
import statistics
from datetime import datetime
import matplotlib.pyplot as plt
import xlrd

def calculate_average_position(file_path, start, end):
    longitudes = []
    latitudes = []

    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            try:
                datetime_date = xlrd.xldate_as_datetime(float(row['Excel Timestamp']), 0)
                time = datetime_date.strptime(datetime_date.strftime( "%H:%M:%S"), "%H:%M:%S").time()
                if start <= time <= end:
                    longitude = float(row[' Longitude'])
                    latitude = float(row[' Latitude'])
                    longitudes.append(longitude)
                    latitudes.append(latitude)
            except ValueError:
                print(f"Skipping invalid data: {row}")
    
    if longitudes and latitudes:
        avg_longitude = statistics.mean(longitudes)
        avg_latitude = statistics.mean(latitudes)
        return avg_latitude, avg_longitude
    else:
        return None

def plot_average_positions(folder_path):
    players = []
    latitudes = []
    longitudes = []
    
    start = input("When was the start of the first half? (HH:MM:SS format) ")
    end = input("When was the end of the first half? (HH:MM:SS format) ")
    start_of_first_half = datetime.strptime(start, "%H:%M:%S").time()
    end_of_first_half = datetime.strptime(end, "%H:%M:%S").time()

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            result = calculate_average_position(file_path, start_of_first_half, end_of_first_half)
            if result:
                lat, lon = result
                players.append(filename[:-4])  
                latitudes.append(lat)
                longitudes.append(lon)

    plt.figure(figsize=(10, 8))
    plt.scatter(longitudes, latitudes, marker='o')

    for i, player in enumerate(players):
        plt.annotate(player, (longitudes[i], latitudes[i]), xytext=(5, 5), textcoords='offset points')

    
    
    home_or_away = input("Is it at home? (Y/N) ")
    if home_or_away == "Y":
        field_coords = [
            (-36.916643, 174.741573),  # Bottom left corner
            (-36.915760, 174.742005),  # Top left
            (-36.915983, 174.742715),  # Top right
            (-36.916861, 174.742285),  # Bottom right
            (-36.916643, 174.741573)   # Closing the polygon
        ]
        field_lats, field_lons = zip(*field_coords)
        plt.plot(field_lons, field_lats, 'r-')

        half_coords = [
            (-36.916204, 174.741788),
            (-36.916422, 174.742504)
        ]
        half_lats, half_lons = zip(*half_coords)
        plt.plot(half_lons, half_lats, 'r-')
        plt.scatter(174.742146,-36.916312, marker='o', c='red')
    elif home_or_away == "N":
        bottom_left = input("Bottom left corner: ")
        top_left = input("Top left corner: ")
        top_right = input("Top right corner: ")
        bottom_right = input("Bottom right corner: ")
        bottom_left = tuple(float(x) for x in bottom_left.split(','))
        top_left = tuple(float(x) for x in top_left.split(','))
        top_right = tuple(float(x) for x in top_right.split(','))
        bottom_right = tuple(float(x) for x in bottom_right.split(','))
        
        
        field_coords = [
            bottom_left,  # Bottom left corner
            top_left,  # Top left
            top_right,  # Top right
            bottom_right,  # Bottom right
            bottom_left   # Closing the polygon
        ]
        field_lats, field_lons = zip(*field_coords)
        plt.plot(field_lons, field_lats, 'r-')

        left_side = input("Left side halfway line point: ")
        right_side = input("Right side halfway line point: ")
        left_side = tuple(float(x) for x in left_side.split(','))
        right_side = tuple(float(x) for x in right_side.split(','))
        
        half_coords = [
            left_side,
            right_side
        ]
        half_lats, half_lons = zip(*half_coords)
        plt.plot(half_lons, half_lats, 'r-')
        """midpoint = input("Kick off point: ")
        midpoint = tuple(float(x) for x in midpoint.split(','))
        plt.scatter(midpoint[0], midpoint[1], marker='o', c='red')"""


    plt.title("Average Positions of Football Players")
    plt.axis('off')
    plt.show()

def main():
    file_name = input("What is the folder called? ")
    dirname = os.path.dirname(__file__)
    folder_path = os.path.join(dirname, file_name)
    plot_average_positions(folder_path)

if __name__ == "__main__":
    main()