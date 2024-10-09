import matplotlib.pyplot as plt
from mplsoccer import VerticalPitch
import numpy as np
import os
import pandas as pd
from datetime import datetime

def calculate_average_position(file_path):
    df = pd.read_csv(file_path)
    start_of_first_half = datetime.strptime("17:02:06", "%H:%M:%S").time()
    end_of_first_half = datetime.strptime("17:48:03", "%H:%M:%S").time()
    df['Excel Timestamp'] = pd.to_datetime(df['Excel Timestamp'], format="%H:%M:%S").dt.time
    first_half = df.loc[(df['Excel Timestamp']>=start_of_first_half) & (df['Excel Timestamp']<=end_of_first_half)]
    avg_longitude = first_half[' Longitude'].mean()
    avg_latitude = first_half[' Latitude'].mean()
    return avg_longitude, avg_latitude

def plot_average_positions(folder_path):
    # Define the corner coordinates
    corners = {
        'bottom_left': (-36.916643, 174.741573),
        'top_left': (-36.915760, 174.742005),
        'top_right': (-36.915983, 174.742715),
        'bottom_right': (-36.916861, 174.742285)
    }

    # Create the pitch
    pitch = VerticalPitch(pad_bottom=0.5, half=False, goal_type='box', goal_alpha=0.8, pitch_type = 'custom', pitch_width = 70, pitch_length = 105)
    fig, ax = pitch.draw(figsize=(12, 8))

    # Convert GPS coordinates to pitch coordinates
    def gps_to_pitch(lon, lat):
        # Calculate pitch dimensions
        pitch_width = 105  # Standard width in meters
        pitch_length = 70  # Standard length in meters

        # Calculate GPS coordinate ranges
        lat_range = corners['top_left'][0] - corners['bottom_left'][0]
        lon_range = corners['bottom_right'][1] - corners['bottom_left'][1]

        # Normalize coordinates to match target values
        x_norm = (lon - corners['bottom_left'][1]) / lon_range
        y_norm = (lat - corners['bottom_left'][0]) / lat_range

        # Scale to pitch dimensions
        x = x_norm * pitch_width
        y = y_norm* pitch_length  # Flip y-axis to match the pitch coordinate system

        return x, y

    # Colors for different players
    colors = plt.cm.rainbow(np.linspace(0, 1, len(os.listdir(folder_path))))

    # Process each CSV file in the folder
    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            avg_longitude, avg_latitude = calculate_average_position(file_path)
            
            # Convert average position to pitch coordinates
            avg_x, avg_y = gps_to_pitch(avg_longitude, avg_latitude)

            ax.scatter(avg_x, avg_y, s=200, c=[colors[i]], marker='o', zorder=2, label=filename[:-4])
            ax.text(avg_x + 1, avg_y + 1, filename[:-4], fontsize=8, color=colors[i])

    # Set title and legend
    ax.set_title("Players' Average Positions", fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
folder_path = r'C:\Users\lukec\Expected Goals Model\ExpectedGoalsModel\Suburbs GPS data'  # Replace with the actual path to your folder
plot_average_positions(folder_path)
