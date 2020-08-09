# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:40:27 2020

@author: Andrea Bassi
"""



"""
example of class that does not allow to set new attributes  
"""

class my_class:
    
    accepted_attributes = ('x','y')
    
    def __init__(self,x0):
        
        self.x = x0
        
        
    def __setattr__(self, name, value):
        "This prohibits the instance to add other attributes than the one specified in accepted_attributes"
        
        if f'{name}' in self.accepted_attributes:
          object.__setattr__(self, name, value)
          # self.name = value # does not set the attribute properly
          print(f'Attribute {name} set to {value}')
        else:
          # raise TypeError(f'Cannot create attribute {name}')
          print (f'Cannot create attribute {name}')

a = my_class(5)

a.y = 3

a.z = 1       

y = getattr(a,'y') 

print('y value:', y)         