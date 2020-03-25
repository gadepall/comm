from __future__ import division
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if


#the ber expression is sqrt(E_b)+n1-n2<0

def qfunc(x):
	return 0.5*mp.erfc(x/mp.sqrt(2))

#Number of SNR samples 
snrlen = 10
#SNR values in dB
snrdb = np.linspace(0,9,10)
#Number of samples
simlen = int(1e5)
#Simulated BER declaration
err = []
#Analytical BER declaration
ber = []
noise1 = np.random.normal(0,1,simlen)
noise2=np.random.normal(0,1,simlen)
#for SNR 0 to 10 dB
for i in range(0,snrlen):
	#Generating AWGN, 0 mean unit variance
	
	#from dB to actual SNR
	snr = 10**(0.1*snrdb[i])
	#Received symbol in baseband
	y1 = mp.sqrt(2*snr) + noise1
	y2=noise2
	#storing the index for the received symbol 
	#in error
	err_ind = np.nonzero(y1 < y2)
	#calculating the total number of errors
	err_n = np.size(err_ind)
	#calcuating the simulated BER
	err.append(err_n/simlen)
	#calculating the analytical BER
	ber.append(qfunc(mp.sqrt(snr)))
	
plt.semilogy(snrdb.T,ber,label='Analysis')
plt.semilogy(snrdb.T,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/bfsk_ber.pdf')
plt.savefig('./figs/bfsk_ber.eps')
subprocess.run(shlex.split("termux-open ./figs/bfsk_ber.pdf"))
#else
#plt.show()
