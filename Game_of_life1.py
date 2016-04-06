# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 13:50:37 2016

@author: OmkarBhatavdekar
"""
import numpy as np
import matplotlib.pyplot as plt
Z =np.array([[0,0,0,1,0,0],
         [0,0,0,1,0,0],
         [0,1,0,1,0,0],
         [0,0,0,1,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0]])
print Z.dtype
print Z.shape
#counting neighbours
N = np.zeros(Z.shape, dtype=int)
x=list()
y=list()

def iterate(Z):
    # Iterate the game of life : naive version
    # Count neighbours
    N = np.zeros(Z.shape, int)
    N[1:-1,1:-1] += (Z[0:-2,0:-2] + Z[0:-2,1:-1] + Z[0:-2,2:] +
                     Z[1:-1,0:-2]                + Z[1:-1,2:] +
                     Z[2:  ,0:-2] + Z[2:  ,1:-1] + Z[2:  ,2:])
    N_ = N.ravel()
    Z_ = Z.ravel()

    # Apply rules
    R1 = np.argwhere( (Z_==1) & (N_ < 2) )
    R2 = np.argwhere( (Z_==1) & (N_ > 3) )
    R3 = np.argwhere( (Z_==1) & ((N_==2) | (N_==3)) )
    R4 = np.argwhere( (Z_==0) & (N_==3) )

    # Set new values
    Z_[R1] = 0.75
    Z_[R2] = 1
    Z_[R3] = Z_[R3]*1.6
    Z_[R4] = 1

    # Make sure borders stay null
    Z[0,:] = Z[-1,:] = Z[:,0] = Z[:,-1] = 0
    return Z
for i in range(100):
    ans=iterate(Z)
    d=sum(Z)
    e=sum(d)
    plt.scatter(i,e)
    #plt.imshow(ans, interpolation= 'nearest')
    plt.pause(.5)

