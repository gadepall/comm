# -*- coding: utf-8 -*-
"""

@authors : Raktim Goswami, Abhisek Bairagi
"""
import numpy as np 
import matplotlib.pyplot as plt 
import cmath
import scipy


def qpsk1(N,mx):
	x_mapping=np.zeros(len(x)/2,dtype=complex)
	i=0
	k=0
	while(i<len(x)):
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

def saw(x):
	x = float(x)
	if x<np.pi and x>=(-np.pi):
		return x
	else: 
		x = x%(2*np.pi)
		if x>np.pi:
			x = x - 2*np.pi
		return x


N=200000
x=np.random.randint(0,2,N)
#print x.shape
mx=np.subtract(np.multiply(x,2),1)
#print mx.shape
qpsk = qpsk1(N,mx)
lp = 18
es = 1
Nsnr = 10
sigma=np.sqrt(0.5*(10.0**(-1/10.0)))
noise=np.random.normal(0,sigma,N/2)+1j*np.random.normal(0,sigma,N/2)
out = np.zeros([Nsnr,])
phi = np.random.rand(1)
phi = saw(phi)
for t in range (10,10+Nsnr):
	v = scipy.vectorize(complex)
	r = np.exp(v(np.zeros(int(N/2)),phi)) 
	received = t*qpsk*r + noise
	snr = np.sqrt((t*qpsk*r/noise)*np.conj((t*qpsk*r/noise))) 

	############### Applying First step of the algorithm ###############################
	k = 0
	r = scipy.vectorize(complex)
	theta_hat1 = r(np.zeros([lp,]))
	theta_hat = np.zeros([lp,])
	for i in range(0,lp):
		theta_hat1 = received[i]*np.conj(t*qpsk[i])
		theta_hat[i] = cmath.phase(theta_hat1)


	############### Applying Second step of the algorithm ##############################

	alpha = 1
	theta = np.zeros([lp,])
	for i in range(1,theta_hat.shape[0]):
		theta[i] = theta[i-1] + alpha*saw(theta_hat[i]-theta[i-1])
	out[t-10] = theta[i]
	#print out[t]
	#print t

phi_m = np.zeros(out.shape)
phi_m[0:] = phi
theta1 = (phi_m-out)**2
x1 = np.linspace(0,theta1.shape[0]-1,theta1.shape[0])
plt.semilogy(x1,theta1)
plt.xlabel('$\\frac{Eb}{N0}$(dB)')
plt.ylabel('$Error$')
plt.legend(['P=%d'%lp],loc='best')
plt.grid(True)
plt.savefig("./Phase_error_with_respect_to_SNR_fixed_pilot.eps")
plt.show()