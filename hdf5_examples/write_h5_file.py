# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 16:14:54 2021

Saves and open h5 file

@author: andrea
"""

import h5py
"""
recommended HDF5 file format for ScopeFoundry:
* = group
- = attr
D = data_set
"""

"""
recommended HDF5 file format for ImageJ/Fiji
data_set in group named: /t0/c0/
with attrubute 'element_size_um' = [size_z,size_y,size_x]
For 2D image shape shoul be [1,...]
    
"""

import numpy as np


#%% Create h5 file 
fname = 'test.h5'
parent = h5py.File(fname,'w')

# create groups
son = parent.create_group('level1') 
gson = son.create_group('level2') 
gdaughter = parent.create_group('lev1/lev2')

# create a dataset
image = np.random.random([4,3])
signal = np.ones([5])
data_set = parent.create_dataset('im', shape=[4,3], data = image)
data_set[:] = image
# parent['voltage2'] = signalA

# create attributes (not in the parents)
son.attrs['exposure'] = 0.1
son.attrs['microscope_type'] = 'SIM'

parent.close()

#%% Read h5 file 

h5file = h5py.File(fname,'r')

# print(dir(h5file))

for key,val in h5file.items():
    
    if isinstance(val, h5py.File) or isinstance(val, h5py.Group):
        print('* ', key, val.name)
                    
    elif isinstance(val, h5py.Dataset):
        
        print('D ', key, val[1,:])
               
    for subkey, subval in val.attrs.items():
        print ('   --', subval,subkey)
        

h5file.close()


