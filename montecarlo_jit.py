# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 11:27:26 2022

@author: andrea
"""

from numba import jit
import random

@jit(nopython=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in range(nsamples):
        x = random.random()
        y = random.random()
        r2 = x ** 2 + y ** 2
        if r2 < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

result = monte_carlo_pi(1000000)

print(result)