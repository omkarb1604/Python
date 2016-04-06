# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:14:21 2016

@author: Omkar Bhatavdekar
"""

import numpy as np
import matplotlib.pyplot as plt


n= 50
t= 50
z= np.zeros((n+1,n+1))
z[2:-2,2:-2]=np.random.randint(0,4,z[2:-2,2:-2].shape)

def iterate(z):
    #summing up the 10*neighbours    
    sum= 10**z[:-2,:-2]+10**z[:-2,1:-1]+10**z[:-2,2:]+10**z[1:-1,2:]+10**z[2:,2:]+10**z[2:,1:-1]+10**z[2:,:-2]+10**z[1:-1,:-2]
    
     #counting the number of things   
    poison= sum/10**3
    rem= sum%10**3
    bacteria= rem/100
    rem= rem%100
    food= rem/10
    rem= rem%10
    earth=rem
    
    #applying the conditions 
    bec_food= (z[1:-1,1:-1]==0) & (food>0)&(bacteria<1)&(poison<1)
    bec_bacteria= (z[1:-1,1:-1]==0)&(food>=2)&(bacteria>=1)
    bec_poison= (z[1:-1,1:-1]==0)&(food>=2)&(poison>=1)
    bec_earth= ((z[1:-1,1:-1]==1)&(bacteria>1))|((z[1:-1,1:-1]==2)&(food<2))|((z[1:-1,1:-1]==3)&(bacteria<2))
    
    #transforming
    z[1:-1,1:-1][bec_food]=1
    z[1:-1,1:-1][bec_bacteria]=1.5
    z[1:-1,1:-1][bec_poison]=3
    z[1:-1,1:-1][bec_earth]=0.75
    
    return z

#making the animation
size = np.array(z.shape)

for i in range(t):
    znew= iterate(z)
    z= znew   
        
    
    #plt.imshow(z, cmap=plt.cm.afmhot)
    #plt.xticks([]), plt.yticks([])
        
   # plt.legend()    
    #plt.show()
    no_food= np.shape(z[z==0])[0] 
    #print no_food, i
    plt.plot(i, no_food,'.r')
    
    no_bacteria= np.shape(z[z==1])[0] 
    #print no_bacteria, i
    plt.plot(i, no_bacteria,'.b')
    
    no_poison= np.shape(z[z==2])[0] 
    #print no_poison, i
    plt.plot(i, no_poison,'.g')
    
    no_earth= np.shape(z[z==3])[0] 
    #print no_earth, i
    plt.plot(i, no_earth,'.y')
    plt.pause(1)
    plt.show()
    