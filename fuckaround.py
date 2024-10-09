import csv
import statistics
from datetime import datetime
import haversine as hs
from haversine import Unit

def calculate_average_position(file_path):
    longitudes = []
    latitudes = []
    start_of_first_half = datetime.strptime("17:02:06", "%H:%M:%S").time()
    end_of_first_half = datetime.strptime("17:48:03", "%H:%M:%S").time()

    # Read the CSV file
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        
        for row in csv_reader:
            try:
                time = datetime.strptime(row['Excel Timestamp'], "%H:%M:%S").time()
                if time >= start_of_first_half and time<= end_of_first_half:
                    longitude = float(row[' Longitude'])
                    latitude = float(row[' Latitude'])
                    longitudes.append(longitude)
                    latitudes.append(latitude)
            except ValueError:
                print(f"Skipping invalid data: {row}")
    
    # Calculate average position
    if longitudes and latitudes:
        avg_longitude = statistics.mean(longitudes)
        avg_latitude = statistics.mean(latitudes)
        return avg_longitude, avg_latitude
    else:
        return None

def main():
    file_path = r'C:\Users\lukec\Expected Goals Model\ExpectedGoalsModel\Suburbs GPS data\Penny.csv'
    
    result = calculate_average_position(file_path)
    loc1 = (-36.915762, 174.742005)
    loc2 = (-36.915984, 174.742715)
    loc3 = (-36.916860, 174.742284)
    loc4 = (-36.916644, 174.741574)
    print(hs.haversine(loc1, loc2, unit=Unit.METERS))
    print(hs.haversine(loc3, loc4, unit=Unit.METERS))
    print(hs.haversine(loc1, loc4, unit=Unit.METERS))
    print(hs.haversine(loc2, loc3, unit=Unit.METERS))
    
    if result:
        avg_longitude, avg_latitude = result
        print(f"Average position:")
        print(f"{avg_latitude:.6f}, {avg_longitude:.6f}")
    else:
        print("No valid data found in the CSV file.")

if __name__ == "__main__":
    main()