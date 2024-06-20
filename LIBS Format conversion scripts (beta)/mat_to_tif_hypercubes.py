# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 18:42:43 2022

@author: Christian
"""

import numpy as np
import seaborn as sns

from PIL import Image
from scipy.io import loadmat
import xarray as xr
import h5py

#X = loadmat('data.mat')['data']
#X = np.transpose(X, axes=[1, 2, 0])

libs_cube = xr.open_dataarray("Kipushi.nc")
libs_cube = libs_cube.sortby('bands')

# h5f = h5py.File('Kipushi.nc', 'r')
# h5f.create_dataset('dataset_1', data=X)


# h5f.close()


imlist = []
for m in X:
    imlist.append(Image.fromarray(m))

imlist[0].save("test.tif", compression="tiff_deflate", save_all=True,
                append_images=imlist[1:])
