#This program calculates the circumcentre of Triangle ABC
import numpy as np
from coeffs import *

def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

A = np.array([-2,-2]) 
B = np.array([1,3]) 
C = np.array([4,-1]) 

#print(ccircle(A,B,C))



