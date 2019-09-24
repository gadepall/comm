# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:38:01 2019

@author: theresh
"""

import numpy as np

def alpha_lookup_tables(t):
    n_bch=(2**(t))-1
    alpha=np.zeros((n_bch,t),dtype=int)
    alpha[1:t+1,:]=np.identity(t)
    for i in range(t+1,n_bch):
        alpha[i,:]=np.mod((alpha[i-t,:]+alpha[i-t+1,:]),2)
    return alpha

t = 14
alpha=alpha_lookup_tables(t)
#print(np.shape(alpha))
