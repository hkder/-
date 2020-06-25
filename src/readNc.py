## Library
import pandas as pd
import numpy as np
import sys
# import iris
import os
import matplotlib.pyplot as plt
from dplython import *
# (DplyFrame, X, diamonds, select, sift, sample_n,
#     sample_frac, head, arrange, mutate, group_by, summarize, DelayFunction)
from scipy.stats import linregress
from matplotlib import pyplot as plt
from IPython.display import Image
# from mpl_toolkits.basemap import Basemap
from matplotlib.colors import Normalize
import matplotlib
import matplotlib.cm as cm
import seaborn as sns
from scipy.stats import linregress
from matplotlib import rcParams
from netCDF4 import Dataset
import struct
import binascii
# from mpl_toolkits.basemap import addcyclic
from netCDF4 import num2date, date2num, date2index
import datetime
# from pyhdf.SD import SD, SDC
import h5py
import netCDF4

def extractPNG(num):
    root_path = '../data/nc/'
    filename = 'gk2aamile1bvi008ko010lc2020061900'

    for i in range(num):
        n = "{0:0=2d}".format(i*2)
        final_path = root_path+filename+n+'.nc'
        nc = Dataset(final_path)
        # examine the variables
        # print(nc.variables.keys())
        # print(nc.variables['image_pixel_values'])
        topo = nc.variables['image_pixel_values'][::10,::10]

        # make image
        plt.figure(figsize=(10,10))
        plt.imshow(topo,origin='lower')
        plt.savefig('../data/png/'+filename+n+'.png', bbox_inches=0)

extractPNG(28)