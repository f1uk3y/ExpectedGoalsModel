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
    pitch = VerticalPitch(pad_bottom=0.5, half=False, goal_type='box', goal_alpha=0.8, axis=True)
    fig, ax = pitch.draw(figsize=(12, 8))

    # Convert GPS coordinates to pitch coordinates
    def gps_to_pitch(lon, lat):
        # Calculate the relative position
        y_rel = (lon - corners['bottom_left'][1]) / (corners['bottom_right'][1] - corners['bottom_left'][1])
        x_rel = (corners['bottom_left'][0] - lat) / (corners['bottom_left'][0] - corners['top_left'][0])
        
        # Convert to pitch coordinates (assuming pitch is 105x70 meters)
        x = x_rel * 105
        y = (1-y_rel) * 70
        return x, y

    # Colors for different players
    colors = plt.cm.rainbow(np.linspace(0, 1, len(os.listdir(folder_path))))

    # Process each CSV file in the folder
    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            avg_longitude, avg_latitude = calculate_average_position(file_path)
            
            # Convert average position to pitch coordinates
            #avg_x, avg_y = gps_to_pitch(avg_longitude, avg_latitude)

            ax.scatter(-36.916197, 174.741985, s=200, c=[colors[i]], marker='o', zorder=2,)
            ax.scatter(avg_longitude, avg_latitude, s=200, c=[colors[i]], marker='o', zorder=2, label=filename[:-4])
            ax.text(avg_longitude + 1, avg_latitude + 1, filename[:-4], fontsize=8, color=colors[i])
 
    
    # Set title and legend
    ax.set_title("Players' Average Positions", fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
    ax.set_xlim(174.741573, 174.742285)
    ax.set_ylim(-36.916643, -36.915760)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Example usage
folder_path = r'C:\Users\lukec\Expected Goals Model\ExpectedGoalsModel\Suburbs GPS data'  # Replace with the actual path to your folder
plot_average_positions(folder_path)