# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 23:41:07 2022

@author: andrea
"""
import numpy as np
a = np.random.random([2,2])
print(a)

sy=4
sx=3


b=np.take(a, range(sy), mode='clip', axis=0) 
c=np.take(b, range(sx), mode='clip', axis=1) 

print(c)