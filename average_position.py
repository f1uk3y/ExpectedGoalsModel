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
    corners = {
        'bottom_left': (174.741573,-36.916643),
        'top_left': (174.742005,-36.915760),
        'top_right': (174.742715,-36.915983),
        'bottom_right': (174.742285,-36.916861)
    }

    pitch = VerticalPitch(pad_bottom=0.5, half=False, goal_type='box', goal_alpha=0.8)
    fig, ax = pitch.draw(figsize=(12, 8))

    def gps_to_pitch(lon, lat):
        pitch_width = 105
        pitch_length = 70

        lat_range = corners['top_left'][1] - corners['bottom_left'][1]
        lon_range = corners['bottom_right'][0] - corners['bottom_left'][0]

        y = (1-(corners['bottom_left'][0]-lon) / lon_range) * pitch_width
        x = (lat - corners['bottom_left'][1]) / lat_range * pitch_length


        return x, y

    colors = plt.cm.rainbow(np.linspace(0, 1, len(os.listdir(folder_path))))

    for i, filename in enumerate(os.listdir(folder_path)):
        if filename.endswith('.csv'):
            file_path = os.path.join(folder_path, filename)
            avg_longitude, avg_latitude = calculate_average_position(file_path)
            
            avg_x, avg_y = gps_to_pitch(avg_longitude, avg_latitude)

            ax.scatter(avg_y, avg_x, s=200, c=[colors[i]], marker='o', zorder=2, label=filename[:-4])
            ax.text(avg_y + 1, avg_x + 1, filename[:-4], fontsize=8, color=colors[i])
    ax.scatter(120,80,  s=200)
    ax.set_title("Players' Average Positions", fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3)
    plt.tight_layout()
    plt.show()

dirname = os.path.dirname(__file__)
folder_path = os.path.join(dirname, 'Suburbs GPS data')
plot_average_positions(folder_path)