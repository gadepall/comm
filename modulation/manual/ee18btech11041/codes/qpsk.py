from __future__ import division
import random
import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
import cmath


#if using termux
import subprocess
import shlex
#end if



def qfunc(x):
	return 0.5*mp.erfc(x/np.sqrt(2))



def bitstream(n):
	bits = np.random.randint(0,2,n)
	return bits
	


def mapping(bits):
	symbol =[]
	for i in range(0,bits.size-1,2):
		msb = bits[i];
		lsb = bits[i+1];
		if msb == 0 and lsb == 0 :
			symbol.append("s0")
		elif msb == 0 and lsb == 1:
			symbol.append("s1")
		elif msb == 1 and lsb ==1:
			symbol.append ("s2")
		elif msb == 1 and lsb == 0:
			symbol.append ("s3")
	return symbol		


snr_db = np.linspace(0,9,10)


err =[]

bits = []
bits = bitstream(100000)


symbol = mapping(bits)



s_in,s_q =0,0
ber=[]
for k in range(len(snr_db)):
	snr = 10**(0.1*snr_db[k])
	received = []
	t=0
	for i in range(len(symbol)):
		
		if symbol[i] == "s0":
			s_in = 1
			s_q = 0
		elif symbol[i] =="s1":
			s_in = 0 
			s_q = 1
		elif symbol[i] == "s2":
			s_in = -1
			s_q = 0
		elif symbol[i] == "s3":
			s_in = 0
			s_q = -1
		noise1 = np.random.normal(0,1,1)	
		noise2 = np.random.normal(0,1,1)
		
		y1 = mp.sqrt(2*snr)*s_in + noise1
		y2 = mp.sqrt(2*snr)*s_q + noise2
	


		if(y1>y2 and y1>-y2):
		
			received.append("s0")
			
			
		
		elif(y1>-y2 and y2>y1):
		
			received.append("s1")
			
			
		elif(y1<-y2 and y2>y1):
		
			received.append("s2")
			
		
		elif(y1<-y2 and y1>y2):
			received.append("s3")
	

		if symbol[i]!=received[i]:
			t+=1;

	err.append((t/50000.0))
	ber.append(1-(1-qfunc(mp.sqrt(snr)))**2)




plt.semilogy(snr_db.T,ber,label='Analysis')
plt.semilogy(snr_db.T,err,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_0}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()

#if using termux
plt.savefig('./figs/qpsk.pdf')
plt.savefig('./figs/qpsk.eps')
subprocess.run(shlex.split("termux-open ./figs/qpsk.pdf"))
#else
#plt.show()


	

											

