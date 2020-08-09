# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:32:36 2020

@author: Andrea Bassi
"""

import numpy as np
       

class SaturationError(Exception):
    pass


class Image_data:
    
    def __init__(self, name, size):
        self.name = name
        
    @property
    def data(self):
        print ('Getting data ...')
        return self._data
            
    @data.setter
    def data(self, data_in):  
        
        print ('Setting data ...')
        saturated = np.count_nonzero(data_in == 255)
        print (f'There are {saturated} saturated pixels')
 
        if  saturated > 0.01 * data_in.size:    
            raise(SaturationError('There are too many saturated pixels'))
        else:     
            self._data = data_in        

size = [128,128]
im = Image_data('roi', size)


for index in range(0,3): 
    
    im.data = np.random.randint(256, size = size) # create a random 8bit image
    
    max_value = np.amax(im.data)
    
    