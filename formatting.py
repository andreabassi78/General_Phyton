# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:18:26 2020

@author: Andrea Bassi
"""


x = 100.3579

s = 'value'

name = 'data_' + s + '_'+ str(x)
print ('straight formatting option:', name)

# %% formatting with .format or f"

name = 'data_{0}_{1}'.format(s,x)
print ('using format():            ', name)

name = f'data_{s}_{x}'
print ('using f:                   ', name)

name = f'data_{s}_{x:.2f}'
print ('using f and specifiers:    ', name)

name = f'data_{s}_{int(x):05d}'
print ('using f and integers:      ', name)



# %% list formatting

mylist = [ 33, 44, 55]

text = f'list_{mylist}'
print ('\nformatting entire lists:                ', text)


text = 'list_{2}_{1}_{0}'.format(*mylist) # note that * returns separate elements from the list
print ('formatting lists with separate elements:', text)

text = f'list_{mylist[2]}_{mylist[1]}_{mylist[0]}'
print ('formatting lists with separate elements:', text)

# %% join method

# 'str_a'.join(list_b) creates a string with all elements (must be string) of list_b separated by str_a 
text = '_'.join(map(str,mylist)) # map applies the function (str) to all the elements of the list
# text = '_'.join(['{}']*len(mylist)).format(*mylist) # equivalent to the previous line

finaltext = 'list_' + text
print ('formatting lists with join             :', finaltext)


import os
path = os.path.join('Programs','temp','test') # join is different from the previous join because it takes multiple arguments, not lists or tuples 
print ('\nformatting directory:', path)