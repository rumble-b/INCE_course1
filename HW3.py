# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 10:31:52 2019
@author: dmennitt

INCE Noise Control Engineering Course I
Lesson 3


"""


##===========================================================================##
## modules
##===========================================================================##
from IPython import get_ipython; get_ipython().magic('reset -sf') 
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.close("all")

##===========================================================================##
## 1 
##===========================================================================##
data = '125 10 15 20 160 12 16 23 200 15 18 26 250 14 15 30 315 12 13 32 400 16 18 25 500 20 23 35 630 22 25 37 800 24 30 40 1000 22 35 43 1250 26 40 46 1600 27 41 50 2000 30 42 54 2500 32 42 55 3150 32 43 54 4000 33 45 55 5000 35 46 56' 
data = array([int(i) for i in data.split()])
data = reshape(data, [17,4])

fig, ax = plt.subplots()
for iP in range(1,4):
    ax.plot(data[:,0], data[:,iP], marker='.', label='partition ' + str(iP))
    ax.set_xlabel('Frequency, Hz'), ax.set_ylabel('Transmission Loss, dB')
    ax.legend(loc='lower right')
    
    
##===========================================================================##
## 2
##===========================================================================##
data = array([[125, 25, 20], [250, 31, 32], [500, 43, 42], [1000, 50, 44], 
                [2000, 61, 45], [4000, 70, 55]])
x = arange(data.shape[0])  

fig, ax = plt.subplots()
barWidth = 0.3
r1 = ax.bar(x - barWidth/2, data[:,1], barWidth, label='Level 1')
r2 = ax.bar(x + barWidth/2,  data[:,2], barWidth, label='Level 2')
 
labels = data[:,0].astype(str)
ax.set_xlabel('Frequency, Hz')
ax.set_ylabel('Sound pressure level, dB')
ax.set_xticks(x); ax.set_xticklabels(labels)
ax.legend()


##===========================================================================##
## 3
##===========================================================================##
def fun(x,y):
    return exp(-x)*sin(y)

dx = 0.1
x = arange(0, 1+dx, dx); y = arange(0, 4*pi+dx, dx)
X, Y = meshgrid(x, y)
z = array(fun(ravel(X), ravel(Y))); Z = z.reshape(X.shape)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')







