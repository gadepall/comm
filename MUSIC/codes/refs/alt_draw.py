#Code by GVV Sharma
#January 28, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Foot of the Altitude
def alt_foot(A,B,C):
  m = B-C
  n = np.matmul(omat,m) 
  N=np.vstack((m,n))
  p = np.zeros(2)
  p[0] = np.matmul(m,A) 
  p[1] = np.matmul(n,B)
  #Intersection
  P=np.matmul(np.linalg.inv(N.T),p)
  return P

#Triangle vertices
A = np.array([-2,-2]) 
B = np.array([1,3]) 
C = np.array([4,-1]) 

#Foots of the altitudes
P = alt_foot(A,B,C)
Q = alt_foot(B,C,A)
R = alt_foot(C,A,B)

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_AP = line_gen(A,P)
x_BQ = line_gen(B,Q)
x_CR = line_gen(C,R)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_BQ[0,:],x_BQ[1,:],label='$BQ$')
plt.plot(x_CR[0,:],x_CR[1,:],label='$CR$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#if using termux
plt.savefig('../figs/alt_triangle.pdf')
plt.savefig('../figs/alt_triangle.eps')
subprocess.run(shlex.split("termux-open ../figs/alt_triangle.pdf"))
#else
#plt.show()







