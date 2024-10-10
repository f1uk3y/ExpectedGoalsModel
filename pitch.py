import csv
import os
import statistics
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def calculate_average_position(file_path):
    longitudes = []
    latitudes = []
    start_of_first_half = datetime.strptime("17:02:06", "%H:%M:%S").time()
    end_of_first_half = datetime.strptime("17:48:03", "%H:%M:%S").time()

    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            try:
                time = datetime.strptime(row['Excel Timestamp'], "%H:%M:%S").time()
                if start_of_first_half <= time <= end_of_first_half:
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

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            result = calculate_average_position(file_path)
            
            if result:
                lat, lon = result
                players.append(filename[:-4])  
                latitudes.append(lat)
                longitudes.append(lon)

    plt.figure(figsize=(10, 8))
    plt.scatter(longitudes, latitudes, marker='o')

    for i, player in enumerate(players):
        plt.annotate(player, (longitudes[i], latitudes[i]), xytext=(5, 5), textcoords='offset points')

    field_coords = [
        (-36.916643, 174.741573),  # Bottom left corner
        (-36.915760, 174.742005),  # Top left
        (-36.915983, 174.742715),  # Top right
        (-36.916861, 174.742285),  # Bottom right
        (-36.916643, 174.741573)   # Closing the polygon
    ]
    field_lats, field_lons = zip(*field_coords)
    
    fig, ax = plt.subplots(figsize=(10, 8))

    field_image = mpimg.imread(r'C:\Users\lukec\Expected Goals Model\ExpectedGoalsModel\background_img.png') 
    ax.imshow(field_image, extent=[min(field_lons), max(field_lons), min(field_lats), max(field_lats)], aspect='auto', alpha=0.5)

    ax.scatter(longitudes, latitudes, marker='o')

    for i, player in enumerate(players):
        ax.annotate(player, (longitudes[i], latitudes[i]), xytext=(5, 5), textcoords='offset points')

    ax.plot(field_lons, field_lats, 'r-')

    ax.set_title("Average Positions of Football Players")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.axis('off')
    plt.show()

def main():
    dirname = os.path.dirname(__file__)
    folder_path = os.path.join(dirname, 'Suburbs GPS data')
    plot_average_positions(folder_path)

if __name__ == "__main__":
    main()