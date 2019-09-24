# -*- coding: utf-8 -*-
"""
Minimal Polynomial matrix 
Created on Sat Dec 22 01:46:47 2018
Released under GNU GPL
@author: theresh
"""

import numpy as np   

def min_poly():
  
	p1=np.array([1,1,0,1,0,1,0,0,0,0,0,0,0,0,1])
	p2=np.array([1,0,0,0,0,0,1,0,1,0,0,1,0,0,1])
	p3=np.array([1,1,1,0,0,0,1,0,0,1,1,0,0,0,1])
	p4=np.array([1,0,0,0,1,0,0,1,1,0,1,0,1,0,1])
	p5=np.array([1,0,1,0,1,0,1,0,1,1,0,1,0,1,1])
	p6=np.array([1,0,0,1,0,0,0,1,1,1,0,0,0,1,1])
	p7=np.array([1,0,1,0,0,1,1,1,0,0,1,1,0,1,1])
	p8=np.array([1,0,0,0,0,1,0,0,1,1,1,1,0,0,1])
	p9=np.array([1,1,1,1,0,0,0,0,0,1,1,0,0,0,1])
	p10=np.array([1,0,0,1,0,0,1,0,0,1,0,1,1,0,1])
	p11=np.array([1,0,0,0,1,0,0,0,0,0,0,1,1,0,1])
	p12=np.array([1,1,1,1,0,1,1,1,1,0,1,0,0,1,1])
	G=np.stack((p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12),axis=0)
	return G

#print(min_poly())
