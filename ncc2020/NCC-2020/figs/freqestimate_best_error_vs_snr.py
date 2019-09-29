# -*- coding: utf-8 -*-
"""

@authors : Sai Manasa Pappu , Siddharth Mourya
"""

import numpy as np 
import scipy
import math
import matplotlib.pyplot as plt
from scipy import special

variance = 1
simlen = 36
Ts = 1e-9
theta = 0

v = scipy.vectorize(complex)
v = v(np.random.normal(0, variance, int(simlen)) , np.random.normal(0, variance, int(simlen)))
k = np.array(range(0 , int(simlen))) 

A = np.linspace(1,5,simlen)

#print(k)
#theta = np.random.uniform(0,2*np.pi)

def R_k(k,r):
	tot=0
	for i in range(k,int(simlen)):
		tot = tot + r[i]*np.conjugate(r[i-k])
	return tot/simlen
	
def estimate(A):
	delf = int(5e6)
	r = scipy.vectorize(complex)
	r = A*np.exp(r(np.zeros(int(simlen)),2*math.pi*delf*k*Ts + theta)) + v 
	#print abs(r)
	#print(r)
	M = 18
	fnm = 0
	fdm = 0
	for i in range(0,int(M)):
		fnm = fnm + np.imag(R_k(i,r)) 
		fdm = fdm + i*np.real(R_k(i,r)) 
	f_hat = fnm/(2*np.pi*Ts*fdm)
	print(str(delf)+" "+str(f_hat))
	
	return abs(f_hat-delf)/delf

err = scipy.vectorize(estimate)
plt.title("SNR vs Frequency Error with fixed frequency offset")
plt.plot(A, err(A),label="QPSK Mapping,$\Delta f =5 MHz$")
plt.xlabel('$SNR$')
plt.ylabel('Error= $(\\frac{\Delta_f - \hat{f}}{\Delta_f})$')
plt.legend(loc='best')
plt.grid()
plt.savefig("./frequencyestiamtion_best_error_vs_snr.eps")
plt.show()
