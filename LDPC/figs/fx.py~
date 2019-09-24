# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:44:29 2019

@author: theresh
"""

import numpy as np
import math as mp
from matplotlib import pyplot as plt
a=np.linspace(-4,4,100)
y=np.zeros(len(a),dtype=float)
for i in range(len(a)):
    y[i]=- np.log(mp.tanh(a[i]))
    
plt.plot(a,y) 
plt.grid(True) 
plt.xlabel('$x$')
plt.ylabel('$f(x)$')  
plt.legend(['$f(x)=-\log (tanh (\\frac{x}{2}))$'],loc='best')
plt.savefig('./fxgraph.eps')

