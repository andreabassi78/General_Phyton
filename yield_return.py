# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 20:34:11 2020

@author: Andrea Bassi

Example on the use of generators, which are a particular case of interators. 
"""

import numpy as np


def signal_generator (omega,phi,dt,T):   
    """ signal_generator returns a generator, not the values t, signal """

    t = 0
    while t<T:
        signal = np.cos (2*np.pi*omega*t+phi)
        yield t, signal
        t += dt
           
        
mygen = signal_generator(omega=2.2, phi = 0, dt= 0.1, T = 1)

# We can now iterate throught the values provided by the generator in different ways

# print(next(mygen))
# print(mygen.__next__())

for t, y in mygen:
    print(f'{t:.2f}, {y: .3f}')
   
 