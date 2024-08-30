import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pitch_width = 120
pitch_length = 80


def onclick(event):
    # Get the x and y coordinates where the user clicked
    x = event.xdata
    y = event.ydata
    if x is not None and y is not None:
        print(f"{y:.2f}, {x:.2f}")


img = mpimg.imread('football_pitch_image.png')


fig, ax = plt.subplots()
ax.imshow(img, extent=[0, pitch_length, 59, (pitch_width)])  # Display the image as the background

# Set plot limits and labels
ax.set_xlim(0, pitch_length)
ax.set_ylim(59, pitch_width)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('Width (meters)')
ax.set_ylabel('Length (meters)')
ax.set_title('Click on the football pitch to get coordinates')

fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
