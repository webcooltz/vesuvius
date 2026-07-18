from vesuvius import Volume, list_files
from pprint import pprint
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.animation as animation

# -----List files-----

# files = list_files()
# pprint(files)

# -----Load scroll-----

# scroll = Volume("Scroll1")
# img = scroll[1000, :, :]

# plt.imshow(img, cmap="gray")
# plt.show()

# -----list segments-----

# files = list_files()

# scroll1 = files["1"]  # print files.keys() if this errors
# print(scroll1)

# -----show segment-----

segment = Volume("20240110113230", verbose=True)

print(segment.shape())

shape = segment.shape()
z, y, x = shape

images = [
    ("Axis 0", segment[z // 2, :, :]),
    ("Axis 1", segment[:, y // 2, :]),
    ("Axis 2", segment[:, :, x // 2]),
]

for title, image in images:
    plt.figure(figsize=(10, 6))
    plt.imshow(image, cmap="gray")
    plt.title(f"{title}: {image.shape}")
    plt.axis("off")

plt.show()

z = segment.shape()[0]

fig, ax = plt.subplots(figsize=(12, 8))
plt.subplots_adjust(bottom=0.15)

img = ax.imshow(segment[0, :, :], cmap="gray")
ax.axis("off")

slider_ax = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(slider_ax, "Depth", 0, z - 1, valinit=0, valstep=1)

def update(val):
    depth = int(slider.val)
    img.set_data(segment[depth, :, :])
    ax.set_title(f"Depth {depth}")
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()

fig, ax = plt.subplots()
im = ax.imshow(segment[0, :, :], cmap="gray")
ax.axis("off")

def animate(i):
    im.set_array(segment[i, :, :])
    ax.set_title(f"Depth {i}")
    return [im]

ani = animation.FuncAnimation(fig, animate, frames=z, interval=80)

plt.show()
