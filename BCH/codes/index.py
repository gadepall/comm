# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 22:01:10 2019

@author: theresh
"""

import numpy as np
from alpha_tables import alpha_lookup_tables
import kbch_nbch_selection
from generator_polynomial import gen_poly

def index(x,code_rate,N):
    alpha=alpha_lookup_tables(code_rate,N)
    kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)
    y=0
    g,Gg=gen_poly(N)
    m1,m=Gg.shape
    m=m-1
    n_bch=nbch #(2**(m))-1
    for i in range(n_bch):
        if((x==alpha[i,:]).all()):
            y=i-1
    return y