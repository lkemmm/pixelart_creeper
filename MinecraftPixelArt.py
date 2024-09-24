import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Create a 720x720 white image with 3 color channels (RGB)
creeper = np.full((720, 720, 3), 255, dtype="uint8")

# Define various green shades
greens = [
    [204, 255, 204], [153, 255, 153], [102, 255, 102], [51, 255, 51],
    [0, 255, 0], [0, 204, 0], [0, 153, 0], [0, 102, 0]
]

# Set up plot for gradual updates
fig, ax = plt.subplots()
img = ax.imshow(creeper)
plt.axis('off')

# Update image on the plot
def update_image():
    img.set_data(creeper)
    plt.draw()
    plt.pause(0.01)

# Fill 90x90 pixel blocks with random green shades
for i in range(0, 720, 90):
    for j in range(0, 720, 90):
        creeper[i:i+90, j:j+90] = random.choice(greens)
        update_image()
        time.sleep(0.05)

# Define creeper face positions and draw face
face_positions = [
    (90, 270, 90, 270), (90, 270, 450, 630),  # Eyes
    (270, 360, 270, 450),                     # Nose
    (360, 540, 180, 540),                     # Mouth
    (540, 630, 180, 270), (540, 630, 450, 540) # Mouth trails
]

# Color the face with black
for pos in face_positions:
    i_start, i_end, j_start, j_end = pos
    creeper[i_start:i_end, j_start:j_end] = [0, 0, 0]
    update_image()
    time.sleep(0.1)

plt.show()
