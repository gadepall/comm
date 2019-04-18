# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 18:38:11 2019

@author: Sandeep Kumar Khyalia, Theresh Babu Benguluri
"""
import numpy as np 
import matplotlib.pyplot as plt 


def qpsk1(N,mx):
	x_mapping=np.zeros(int(len(x)/2),dtype=complex)
	i=0
	k=0
	while(i<len(x)-1):
	    if mx[i]==1 and mx[i+1]==1:
	        x_mapping[k]=complex(1,1)
	    elif mx[i]==1 and mx[i+1]==-1:
	        x_mapping[k]=complex(1,-1)
	    elif mx[i]==-1 and mx[i+1]==1:
	        x_mapping[k]=complex(-1,1)
	    elif mx[i]==-1 and mx[i+1]==-1:
	        x_mapping[k]=complex(-1,-1)
	    i=i+2
	    k=k+1
	x_mapping1=np.divide(x_mapping,np.sqrt(2))
	qpsk = x_mapping1
	return qpsk


N=200000
x=np.random.randint(0,2,N)
mx=np.subtract(np.multiply(x,2),1)
qpsk = qpsk1(N,mx)
aa=qpsk

p = 18
gamma = 0.001

Eb_N0_dB= 1
alpha1 = np.zeros([p,],dtype=complex)
alpha2 = np.zeros([p,],dtype=complex)
alpha3 = np.zeros([p,],dtype=complex)
alpha = np.zeros([p,],dtype=complex)
s=np.zeros([p,],dtype=complex)
a=np.zeros([p,])
sk=np.complex(0.7,0.8) 
#es = 10
#n0 = np.sqrt(0.5*(10.0**(-1/10.0)))
#A = np.linspace(1,5,simlen)
#sigma = 1/(2*p*p*es/n0)
#sigma=1/(2*es/n0)
#noise=np.random.normal(0,sigma,int(N/2))+1j*np.random.normal(0,sigma,int(N/2))
n0 = 10**(-1/10.0)
noise=np.random.normal(0,np.sqrt(n0/2),int(N/2))+1j*np.random.normal(0,np.sqrt(n0/2),int(N/2))
received = sk*qpsk + noise
for i in range(1,alpha.shape[0]):
    alpha1[i-1]=alpha[i-1]*received[i-1]-qpsk[i-1]
    alpha2[i-1]=alpha1[i-1]*(np.conj(qpsk[i-1]))
    alpha3[i-1]=gamma*alpha2[i-1]
    alpha[i]=alpha[i-1]-alpha3[i-1]
    a[i]=abs(alpha[i])
    s[i]=a[i]*received[i]
sk_m = np.zeros(s.shape,dtype=complex)
sk_m[0:] = sk    
error1=np.zeros([p,],dtype=complex)
error2=np.zeros([p,])
for i in range(1,alpha.shape[0]):
    error1[i]=(sk_m[i]-s[i])
    error2[i]=np.abs(sk_m[i]-s[i])
    

x1 = np.linspace(0,alpha.shape[0],alpha.shape[0])
K=np.ones(len(x1))*sk
##===============================================================================
# Plotting
##===============================================================================
plt.plot(x1,np.real(error1),x1,np.imag(error1))
plt.plot(x1,np.real(K),x1,np.imag(K))
#plt.title('Convergence of Digital AGC for QPSK, SNR=%d dB'%Eb_N0_dB)
plt.xlabel('$P$')
plt.ylabel('$\\alpha$')
plt.legend(['$\hat{\\alpha_I }$','$\hat{\\alpha_Q}$','$\\alpha_I$','$\\alpha_Q$'],loc='best')
plt.grid(True)
plt.savefig('./Convergence_of_Digital_AGC.eps')
plt.show()