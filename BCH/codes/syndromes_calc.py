# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:46:41 2019

@author: theresh
"""

import numpy as np
from alpha_tables import alpha_lookup_tables

t=14
alpha=alpha_lookup_tables(t)  # t=14
def syndromes(r,alpha):
    m=12        # Error correcting capability is 12.
    t=14
    n_bch=len(r)
    S=np.zeros((2*m,t),dtype=int)
    #s=np.zeros(2*m,dtype=int)
    for i in range(2*m):
        for j in range(n_bch):
            if r[j]==0:
                S[i,:]=S[i,:]
            else:
                S[i,:]=np.mod((S[i,:]+alpha[(i*j-i)% n_bch,:]),2)
    return S


S=syndromes(np.random.randint(0,2,3240),alpha)
print(S)
    
    
    
  
    
    
    
    

