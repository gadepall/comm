#This program calculates the foot of the altitude of Triangle ABC
import numpy as np
from coeffs import *

A = np.array([-2,-2]) 
B = np.array([1,3]) 
C = np.array([4,-1]) 

m = dir_vec(B,C)
n = norm_vec(B,C)
p = np.zeros(2)
p[0] = np.matmul(m,A)
p[1] = np.matmul(n,B)

#Intersection
N=np.vstack((m,n))
P=np.matmul(np.linalg.inv(N),p)
print(P)



