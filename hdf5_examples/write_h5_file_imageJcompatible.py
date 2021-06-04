# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:14:54 2021
Generates a h5 file with datasets compatible with ImageJ/Fiji
@author: andrea
"""

import h5py
import numpy as np

"""
recommended HDF5 file format for ImageJ/Fiji
data_set in group named: /t0/c0/
with attrubute 'element_size_um' = [size_z,size_y,size_x]
For 2D image shape shoul be [1,...]
    
"""

#%% Create h5 file 
fname = 'test_imageJ.h5'
f = h5py.File(fname,'w')

# create groups
group = f.create_group('t0/c0')

imageA = np.random.random([4,3,3])
imageB = np.random.random([4,3,3])

data_setA = group.create_dataset('imA', shape=[4,3,3], data = imageA)
data_setB = group.create_dataset('imB', shape=[4,3,3], data = imageB)

data_setA.attrs['element_size_um'] = [0.1, 0.5, 1]
data_setB.attrs['element_size_um'] = [0.1, 0.5, 1]

f.close()

