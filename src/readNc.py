import matplotlib.pyplot as plt
import netCDF4
from os import path
from glob import glob

fig = plt.figure()
ax = fig.add_subplot(111)
plt.ion()
plt.show()

for files in glob("./data/nc/*.nc"):
    nc = netCDF4.Dataset(files)
    image = nc.variables['image_pixel_values']
    ax.imshow(image)
    plt.draw()
    plt.pause(0.02)
    plt.imsave("./data/jpg" + path.basename(files)[:-2] + ".jpg", image)
