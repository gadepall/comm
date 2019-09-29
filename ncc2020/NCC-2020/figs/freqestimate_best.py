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
simlen = int(1e4)
Ts = 1e-10
theta = 0

v = scipy.vectorize(complex)
v = v(np.random.normal(0, variance, int(simlen)) , np.random.normal(0, variance, int(simlen)))
k = np.array(range(0 , int(simlen))) 

#print(k)
#theta = np.random.uniform(0,2*np.pi)

def R_k(k,r):
	tot=0
	for i in range(k,int(simlen)):
		tot = tot + r[i]*np.conjugate(r[i-k])
	return tot/simlen
	
def err(delf):
	r = scipy.vectorize(complex)
	r = 5*np.exp(r(np.zeros(int(simlen)),2*math.pi*delf*k*Ts + theta)) + v 
	#print abs(r)
	#print(r)
	M = 10
	fnm = 0
	fdm = 0
	for i in range(0,int(M)):
		fnm = fnm + np.imag(R_k(i,r)) 
		fdm = fdm + i*np.real(R_k(i,r)) 
	f_hat = fnm/(2*np.pi*Ts*fdm)
	print(str(delf)+" "+str(f_hat))
	return abs(f_hat-delf)/f_hat
	
freq_values = np.linspace(1e5,4e7,20) # freq values from 1000 to 40 MHz
error_values = scipy.vectorize(err)

plt.title("$\Delta f$ vs frequency error with fixed SNR ")
plt.plot(freq_values,error_values(freq_values),label="QPSK Mapping, SNR= 6.98 dB ")
plt.xlabel('$\Delta_f$')
plt.ylabel('Error= $(\\frac{\Delta_f - \hat{f}}{\Delta_f})$')
plt.legend(loc='best')
plt.grid()
plt.savefig("./frequency_best.eps")
plt.show()