# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:07:05 2021

@author: andrea
"""

import numpy as np

m = np.random.random([3,4])

filename = 'calibration.txt'

f = open(filename, 'a')
f. write('\nParameter\n')
f.write(str(m))
f.close()