#Code by GVV Sharma
#May 19, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle

#if using termux
import subprocess
import shlex
#end if

#Generate line points


len = 100
#r_1 = 1
#r_1 = 3.6502815398728847

r_1 = 5
ms = 2
r_2 = np.sqrt(5)
c_1 = np.array([3,-2]) 
m = np.array([1,ms]) 
c = np.array([0,1]) 
c_2 = np.array([2,-1]) 
#Generating Circumcircle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r_1*np.cos(theta)
x_circ[1,:] = r_1*np.sin(theta)
#x_circ = get_coord(r,theta).reshape((2,len))
#x_circ = get_coord(r,theta)
#print(np.shape(x_circ))
x_circ = (x_circ.T + c_1).T
#x_circ = (x_circ + O).T

#temp1 = -m.T@(c-c_1)
#temp2 = np.sqrt(temp1**2-(np.linalg.norm(c-c_1))**2+25)
#lam1 = (temp1+temp2)/((np.linalg.norm(m))**2)
#lam2 = (temp1-temp2)/((np.linalg.norm(m))**2)
#P = c + lam1*m
#Q = c + lam2*m

#
#Finding F and G
c0 = np.linalg.norm(m)**2
c1 = 2*m.T@(c-c_1)
c2 = (np.linalg.norm(c-c_1))**2-25
polc = [c0,c1,c2]
[lam1,lam2] = np.roots(polc)
print(lam1,lam2)
P = c + lam1*m
Q = c + lam2*m
#
#c0 = n2.T@n2
#c1 = 2*n2.T@(I-O)
#c2 = ((I-O).T)@((I-O).T)-r**2
#polc = [c0,c1,c2]
#[lam1,lam2] = np.roots(polc)
#G = I + lam2*n2
#
##Line FG
#n_FG = norm_vec(F,G)
#c_FG = n_FG.T@F
#
##P and Q
#c_AB = n1.T@A
#P = line_intersect(n1,c_AB,n_FG,c_FG)
#c_AC = n2.T@A
#Q = line_intersect(n2,c_AC,n_FG,c_FG)
#
##Generating all lines
#x_AB = line_gen(A,B)
#x_BC = line_gen(B,C)
#x_CA = line_gen(C,A)
#x_FG = line_gen(F,G)
x_PQ = line_gen(P,Q)
#x_GI = line_gen(G,I)



#Plotting all lines
#plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
#plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
#plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$\Omega$')
#plt.plot(x_circ2[0,:],x_circ2[1,:],label='$\Omega$')
#plt.plot(x_FG[0,:],x_FG[1,:],label='$FG$')
#plt.plot(x_FH[0,:],x_FH[1,:],label='$FH$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$\Gamma$')
#plt.plot(x_GI[0,:],x_GI[1,:],label='$GI$')

plt.plot(c[0], c[1], 'o')
plt.text((c[0]+0.1) * (1 + 0.1), c[1] * (1 -0.2) , 'c')
#plt.plot(A[0], A[1], 'o')
#plt.text(A[0] * (1 + 0.1), A[1] * (1 ) , 'A')
#plt.plot(B[0], B[1], 'o')
##plt.text(B[0] * (1 - 0.2), B[1] * (1+0.3) , 'B')
#plt.text(B[0]  - 0.2, B[1] +0.3 , 'B')
#plt.plot(C[0], C[1], 'o')
#plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.2) , 'C')
#plt.plot(D[0], D[1], 'o')
#plt.text(D[0] * (1 - 0.1), D[1] * (1  ) , 'D')
#plt.plot(E[0], E[1], 'o')
#plt.text(E[0] * (1 + 0.05), E[1] * (1) , 'E')
#plt.plot(O[0], O[1], 'o')
#plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
#plt.plot(F[0], F[1], 'o')
#plt.text(F[0] * (1 - 0.1), F[1] * (1 - 0.1) , 'F')
#plt.plot(G[0], G[1], 'o')
#plt.text(G[0] * (1 + 0.1), G[1] * (1 - 0.1) , 'G')
#plt.plot(H[0], H[1], 'o')
#plt.text(H[0] * (1 + 0.1), H[1] * (1 - 0.1) , 'H')
#plt.plot(I[0], I[1], 'o')
#plt.text(I[0] * (1 - 0.1), I[1] * (1 - 0.1) , 'I')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.1), P[1] * (1 + 0.1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.1), Q[1] * (1 + 0.1) , 'Q')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
#if using termux
plt.savefig('../figs/2019_3.pdf')
plt.savefig('../figs/2019_3.eps')
subprocess.run(shlex.split("termux-open ../figs/2019_3.pdf"))
#else
#plt.show()







