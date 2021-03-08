# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 11:27:55 2021

@author: Andrea
"""
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 10, 100)
y0 = np.sin(x) * x
y1 = np.sin(x) * x**1.5
y2 = np.sin(x) * x**2

char_size = 20
linewidth = 2

plt.rc('font', family='serif', size=char_size)

fig = plt.figure(figsize=(5,5), dpi=600)
ax = fig.add_subplot(111)

title = 'plot title'
xlabel = 'x'
ylabel = 'y'

ax.plot(x, y0, 
        linewidth=linewidth,
        linestyle='dashed',
        color='black')

ax.plot(x, y1, 
        linewidth=linewidth,
        linestyle='solid',
        color='gray')
 
ax.plot(x, y2, 
        linewidth=linewidth,
        linestyle='solid',
        color='silver')

#ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_title(title, size=char_size*0.8)   
ax.set_xlabel(xlabel, size=char_size)
ax.set_ylabel(ylabel, size=char_size)
ax.xaxis.set_tick_params(labelsize=char_size*0.7)
ax.yaxis.set_tick_params(labelsize=char_size*0.7)

 
ax.grid(True, which='major',axis='both',alpha=0.2)   
ax.legend(['y0','y1','y2'],
          loc='best',frameon = False,
          fontsize=char_size*0.8)

fig.tight_layout()
plt.rcParams.update(plt.rcParamsDefault)