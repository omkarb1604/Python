# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 12:34:21 2016

@author: OmkarBhatavdekar
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
number=10
while (number>1):
    for i in range(4):
        
        a=np.zeros(4)
        
        e=number
        number=number/2
        a+=np.array(number)
        
x=np.arange(4)
y=a
print y
print('My epsilon is %g',e)