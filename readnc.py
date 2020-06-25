import matplotlib.pyplot as plt
import netCDF4
import sys
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
    if input() == 'q':
        break
