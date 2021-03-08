# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 09:50:09 2020

@author: Andrea Bassi
"""
    
x = 5
a = 0    

"note that running x/0 would raise an error and interrupt the code"

    
try:
    y=x/a
    
except ZeroDivisionError as err:
    y = 0
    print('There was an error, but do not worry, we have set y to:', y)
    print('Error was:', err)
    
else:
    print('Result is:', y)    


finally:
    print ('Done')