# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 16:25:40 2016

@author: OmkarBhatavdekar
"""
#initial value problem

import scipy
import scipy.integrate
import matplotlib.pyplot as plt

def deriv (Y, x, a, b):
    [y, z]=Y
    dybydx=z
    dzbydx=a*y+b*scipy.exp(x)
    return [dybydx, dzbydx]
    
y0, z0= 1, 2
Y0=[y0, z0]

x=scipy.linspace(0, 1, 30 )

a, b= 4, 1

soln=scipy.integrate.odeint(deriv, Y0, x, args=(a,b))

y=soln[:,0]
z=soln[:,1]

print y
print z

#plt.show()
#plt.plot(x,y,'r')
#plt.plot(x,z, 'k')

fig=plt.figure()
fig.show()
axy=fig.add_subplot(121)
axz=fig.add_subplot(122)
axy.title.set_text('y vs x')
axz.title.set_text ('z vs x')
axy.xaxis.label.set_text('x') ; axy.yaxis.label.set_text('y') 
axz.xaxis.label.set_text('x') ; axz.yaxis.label.set_text('z') 
axy.plot(x,y, 'r')
axz.plot(x,z ,'k')