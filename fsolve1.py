# -*- coding: utf-8 -*-
"""
Created on Sun May  1 02:09:44 2016

@author: OmkarBhatavdekar
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import fsolve

a=4
b=3
x=np.linspace(0,10,20)
func= a*scipy.exp(-x)-b*x

plt.plot(x, func)
plt.show()
plt.grid()
#x_ini=1
#x_soln=fsolve(func, x_ini)

#print x_soln