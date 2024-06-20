# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 22:03:32 2022

@author: Christian
"""

import xarray as xr

import scipy.io
import numpy as np
from PIL import Image

import skimage.io as skio
imstack1    = skio.imread("Schm01.tif", plugin="tifffile")

imstack1 = np.transpose(imstack1, axes=[0, 2, 1])


# data = np.array(tiffstack)

file_path = 'SCHM01.mat'
scipy.io.savemat(file_path, {'data': imstack1})

libs_cube = xr.DataArray(imstack1,dims=("bands","x","y"))
libs_cube_ds=libs_cube.to_dataset(name='mapping')
libs_cube_ds=libs_cube_ds.mapping.astype('int16')
libs_cube_ds.to_netcdf("Schm01.nc",engine='netcdf4')
