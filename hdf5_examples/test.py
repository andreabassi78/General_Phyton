# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 10:09:42 2021

@author: andrea
"""

import h5py
import numpy as np

fname = 'temp.h5'

parent = h5py.File(fname,'w')


# create groups
son = parent.create_group('level1')

gson = son.create_group('level2')

gdaugther = parent.create_group('lev1/lev2')

# create a dataset

image = np.random.random([4,3])

data_set = parent.create_dataset('im',shape = [4,3], data = image)
# data_set[:] = image

# create attributes (not in the parents)

son.attrs['exposure'] = 0.1
son.attrs['microscope_type'] = 'SIM'

parent.close()


#%% Read h5 file


h5file = h5py.File(fname,'r')

# print( list(h5file.items() ))


for key,val in h5file.items():
    
    if isinstance(val, h5py.File) or isinstance(val, h5py.Group):
        print('* ', key, val.name)
                    
    elif isinstance(val, h5py.Dataset):
        
        print('D ', key, val[1,:])
               
    for subkey, subval in val.attrs.items():
        print ('   --', subkey,subval)
 
h5file.close()









