# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 10:40:27 2020

@author: Andrea Bassi
"""



"""
Example of class that does not allow to set new attributes. 
It is for testing setattr() method only.
This task should be done properly using __slots__
"""

class my_class:
    
    __accepted_attributes = ('x','y') # __private, and static, attribute
    
    def __init__(self,x0):
        
        self.x = x0
        
        
    def __setattr__(self, name, value):
        "Prohibits the instance to add other attributes than the one specified in __accepted_attributes"
        
        if name in self.__accepted_attributes:
            # object here is any other object (the most base type), to avoid recursion error
            object.__setattr__(self, name, value)
            # self.name = value # does not set the attribute properly, it sets only the value
            print(f'Attribute {name} set to {value}')
        
        else:
            # raise TypeError(f'Cannot create attribute {name}')
            print (f'Cannot create attribute {name}')


# %% Instantiation

a = my_class(5)

a.y = 3

a.z = 1       

y = getattr(a,'y') 

print('y value:', y)   


      