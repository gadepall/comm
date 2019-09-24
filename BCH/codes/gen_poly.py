# -*- coding: utf-8 -*-
"""
Generator Polynomial
Created on Sat Dec 22 01:46:47 2018
Released under GNU GPL
@author: theresh
"""

import numpy as np   
from min_poly_mat import min_poly

def gen_poly():
	G=min_poly()
	c=np.convolve(G[0],G[1])
	for i in range(2,12):
		k=np.convolve(G[i],c)
		c=k
	c=c%2
	return c

#print(gen_poly())

