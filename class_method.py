# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:52:21 2020

@author: Andrea Bassi
"""


"""
Example of class method used create a modified version of the class, before creating the instance.
Can be useful to save memory.
"""

import time
import numpy as np

class dataset:
    
    def __init__(self, name, size):
        self.name = name
        self.time = time.time()
        self.data = np.random.random(size)
        
    @classmethod
    def image_data (cls, name, size):
        im_size  = [size,size] 
        return cls(name, im_size)

    def display(self):
        print(f'{self.name} shape:{self.data.shape}')
        

data0 = dataset('signal_data', 10)
data0.display()

# data1 is instanciated using the modified class called with the static method image_data
data1 = dataset.image_data('image_data', 5) 
data1.display()

