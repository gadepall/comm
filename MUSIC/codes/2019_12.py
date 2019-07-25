#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
#end if

m_1 = np.array([[-1,2,2]]) 
m_2 = np.array([[2,-1,2]]) 
m_3 = np.array([[-2,2,1]]) 

M = np.hstack((m_1.T,m_2.T,m_3.T))
c_1 =  np.array([[1,0,0]]) 
c_2 =  np.array([[0,0,0]]) 

y =  np.hstack((m_1@c_2.T,m_2@c_1.T,m_3@c_1.T) )
print(M,y,np.linalg.inv(M.T)@y.T)
#Generate line points
#def line_gen(A,B):
#  len =10
#  x_AB = np.zeros((2,len))
#  lam_1 = np.linspace(0,1,len)
#  for i in range(len):
#    temp1 = A + lam_1[i]*(B-A)
#    x_AB[:,i]= temp1.T
#  return x_AB
#

#Triangle sides
#a = np.sqrt(3)
#b = 1
#c = 1

#Triangle vertices
#A = c*np.array([np.cos(np.pi/6),np.sin(np.pi/6)]) 
#B = np.array([0,0]) 
#C = np.array([a,0]) 
#S = (A+B)/2
#E = perp_foot(A,B,C)
#I,r = icentre(A,B,C)
#print(I)
#O=line_seg_intersect(A,C,S,E)

#Generating all lines
#x_AB = line_gen(A,B)
#x_BC = line_gen(B,C)
#x_CA = line_gen(C,A)
#x_CS = line_gen(C,S)
#x_AE = line_gen(E,A)
#x_BI = line_gen(B,I)
#x_CI = line_gen(C,I)

#Plotting all lines
#plt.plot(x_AB[0,:],x_AB[1,:],label='$PQ$')
#plt.plot(x_BC[0,:],x_BC[1,:],label='$QR$')
#plt.plot(x_CA[0,:],x_CA[1,:],label='$RP$')
#plt.plot(x_CS[0,:],x_CS[1,:],label='$RS$')
#plt.plot(x_AE[0,:],x_AE[1,:],label='$PE$')
#plt.plot(x_BI[0,:],x_BI[1,:],'--',label='$QI$')
#plt.plot(x_CI[0,:],x_CI[1,:],'--',label='$RI$')
#
#plt.plot(A[0], A[1], 'o')
#plt.text(A[0]* (1+ 0.1), A[1]*(1+ 0.1) , 'P')
#plt.plot(B[0], B[1], 'o')
#plt.text(B[0] - 0.1, B[1] * (1) , 'Q')
#plt.plot(C[0], C[1], 'o')
#plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'R')
#plt.plot(S[0], S[1], 'o')
#plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S')
#plt.plot(E[0], E[1], 'o')
#plt.text(E[0] * (1 + 0.03), E[1] * (1 - 0.1) , 'E')
#plt.plot(O[0], O[1], 'o')
#plt.text(O[0] * (1 + 0.03), O[1] * (1 - 0.1) , 'O')
#plt.plot(I[0], I[1], 'o')
#plt.text(I[0] * (1 + 0.03), I[1] * (1 - 0.1) , 'I')
#
#plt.xlabel('$x$')
#plt.ylabel('$y$')
#plt.legend(loc='best')
#plt.grid() # minor
#plt.axis('equal')
##plt.ylim(0,2)
##plt.xlim(0,2)
##if using termux
#plt.savefig('../figs/2019_8.pdf')
#plt.savefig('../figs/2019_8.eps')
#subprocess.run(shlex.split("termux-open ../figs/2019_8.pdf"))
##else
##plt.show()
