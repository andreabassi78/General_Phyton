# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:18:05 2022

@author: andrea
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, convolve

t = np.linspace(0,1)

f = np.exp(-(t-0.5)**2/0.1**2) + 0.5* np.random.random(t.size)

plt.plot(t,f)


g = np.gradient(f)

plt.plot(t,g)


kernel = np.array([3, 2, 1 , 0, -1 ,-2, -3])
kernel = kernel / np.sqrt(np.sum(kernel**2))

filtered = convolve(f, kernel, mode = 'same', method ='direct')

plt.plot(t,filtered)





   
