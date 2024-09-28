import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.widgets import Button, RadioButtons

pitch_width = 120
pitch_length = 80
shot_outcome = None

shot_color = {"onGoal":'#13293fa6', "offGoal":'#13293f66', 'blocked':'#13293f66', "goal":'#ff6300'}

# Define outcomes
outcomes = ["onGoal", "offGoal", "blocked", "goal"]

# Function to handle click events on the pitch
def onclick(event):
    x = event.xdata
    y = event.ydata
    if x is not None and y is not None and shot_outcome:
        print(f"{shot_outcome}, , , {y:.2f}, {x:.2f}")
        ax.plot(x, y, 'ro')  # Mark the shot on the pitch
        fig.canvas.draw()

# Function to handle outcome selection
def update_shot_outcome(label):
    global shot_outcome
    shot_outcome = label
    print(f"Selected outcome: {shot_outcome}")

# Load the football pitch image
img = mpimg.imread('football_pitch_image.png')

# Set up the plot
fig, ax = plt.subplots()
ax.imshow(img, extent=[0, pitch_length, 59, pitch_width])  # Display the image as the background

# Set plot limits and labels
ax.set_xlim(0, pitch_length)
ax.set_ylim(59, pitch_width)
ax.set_xlabel('Width (meters)')
ax.set_ylabel('Length (meters)')
ax.set_title('Click on the football pitch to get coordinates')

# Add radio buttons for shot outcome selection
rax = plt.axes([0.75, 0.01, 0.2, 0.2], facecolor='lightgoldenrodyellow')  # Position of the radio buttons
radio = RadioButtons(rax, outcomes)
radio.on_clicked(update_shot_outcome)

# Connect the click event
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

