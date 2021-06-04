# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:27:26 2020

@author: Andrea Bassi
"""

import numpy as np
import time 


def calculate_extremes(function):
    """Fucntion decorator to calculate and print min and max value of a siganl""" 
    def inner(*args,**kwargs):
        
        print ( f'Signal generated with function: {function.__name__} ' )
        print ( f'Function decorated with function: {calculate_extremes.__name__} ' )  
        
        signal = function(args[0])
        extremes = np.amin(signal), np.amax(signal)
        print ( f'Min and max values: {extremes}' )  
        
        return signal # this is the return of function when decorated
        
    return inner



class Calculate_extremes:
    """Class decorator to calculate and print min and max value of a siganl"""  
    def __init__(self,function):
        
        print ( f'Signal generated with function: {function.__name__} ' ) 
        print ( f'Function decorated with Class: {self.__class__.__name__} \n' )  
        
        self.function = function
    
    def __call__(self, *args, **kwargs):
        
        signal =  self.function(args[0])
        extremes = np.amin(signal), np.amax(signal)
        print ( f'Min and max values: {extremes}\n' ) 
        return signal
    

class Timer: 
    """Class decorator to measure execution time"""  
    def __init__(self, function): 
        self.function = function 
  
    def __call__(self, *args, **kwargs): 
        start_time = time.time() 
        result = self.function(*args, **kwargs) 
        end_time = time.time() 
        print(f'Execution time: {end_time-start_time:.6f} s \n') 
        return result 
    


#@calculate_extremes
@Timer 
@Calculate_extremes
def generate_signal(samples_number):
    sig = np.random.random(samples_number)
    return sig

    
print('Lenght of generated signal:', len (generate_signal(1000000)) )
