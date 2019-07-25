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

#Triangle sides
a = 8
b = 11
c = 13
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
#x = 7
x = 3
#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 
D = (x*B+(c-x)*A)/c
E = (x*C+(b-x)*A)/b
H = (D+B)/2
I = (E+C)/2
n1 = norm_vec(A,B)
n2 = norm_vec(A,C)

#print((n1.T)@D)

O,r = ccircle(A,B,C)
c0 = n1.T@n1
c1 = 2*n1.T@(H-O)
c2 = ((H-O).T)@((H-O).T)-r**2
polc = [c0,c1,c2]
[lam1,lam2] = np.roots(polc)
F = H + lam2*n1

#lam1 = (-c1 + np.sqrt(c1**2 - 4 * c0*c2))/(2*c0)
#print(lam1,lam2,n1,D)
c0 = n2.T@n2
c1 = 2*n2.T@(I-O)
c2 = ((I-O).T)@((I-O).T)-r**2
polc = [c0,c1,c2]
[lam1,lam2] = np.roots(polc)
G = I + lam2*n2


#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_FG = line_gen(F,G)
x_DE = line_gen(D,E)

#Generating Circumcircle
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_circ[0,:],x_circ[1,:],label='$circumcircle$')
plt.plot(x_FG[0,:],x_FG[1,:],label='$FG$')
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 ) , 'A')
plt.plot(B[0], B[1], 'o')
#plt.text(B[0] * (1 - 0.2), B[1] * (1+0.3) , 'B')
plt.text(B[0]  - 0.2, B[1] +0.3 , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.2) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.1), D[1] * (1  ) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 + 0.05), E[1] * (1) , 'E')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 - 0.1), F[1] * (1 - 0.1) , 'F')
plt.plot(G[0], G[1], 'o')
plt.text(G[0] * (1 + 0.1), G[1] * (1 - 0.1) , 'G')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#
#if using termux
plt.savefig('../figs/2018_6.pdf')
plt.savefig('../figs/2018_6.eps')
subprocess.run(shlex.split("termux-open ../figs/2018_6.pdf"))
#else
#plt.show()







