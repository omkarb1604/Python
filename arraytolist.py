# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 22:01:34 2016

@author: OmkarBhatavdekar
"""

import time
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1000, 0, 1])
plt.ion()
plt.show()

for i in range(1000):
    y = 2+i
    plt.scatter(i, y)
    plt.draw()
    

        
        

