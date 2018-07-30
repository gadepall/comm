from __future__ import division
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt




def qfunc(x):
	return 0.5*mp.erfc(x/np.sqrt(2))

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
temp=0
noise1 = np.random.normal(0,1,simlen)
noise2=np.random.normal(0,1,simlen)

#for SNR 0 to 10 dB
for i in range(0,snrlen):
	snr = 10**(0.1*snrdb[i])	#Received symbol in baseband
	rx = mp.sqrt(2*snr) + noise1
	ry = noise2
	temp=0
	for j in range (0,len(rx)):
	    if ((rx[j]>ry[j]) and (rx[j]>-ry[j])):
	    	temp=temp+1                
                				
	#calculating the total number of errors
	#err_n = np.size(err_ind)
	#calcuating the simulated BER
	err.append(1-temp/simlen)
	#calculating the analytical BER
	ber.append(1-(1-qfunc(mp.sqrt(snr)))**2)
	
plt.semilogy(snrdb.T,ber,label='Analysis')
plt.semilogy(snrdb.T,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()
plt.savefig('qpsk_err.eps')
plt.show()
