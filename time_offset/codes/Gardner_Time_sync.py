# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:22:28 2019

@author: theresh
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import special

N=100000
data=np.random.randint(0,2,N)
c=2*data-1
Tsym=100
#sym_samp=np.arange(0,Tsym)
Eb_N0_dB=np.linspace(0,8,9)
BER_sim=np.zeros(len(Eb_N0_dB))
pulse=np.ones(Tsym)
inter_data=np.zeros(N*Tsym)
for i in range(N):
    inter_data[i*Tsym:(i+1)*Tsym]=c[i]
#plt.plot(inter_data)
#plt.show()

#toff=np.zeros(len(Eb_N0_dB))
#poff=np.zeros(len(Eb_N0_dB))
for i in range(len(Eb_N0_dB)):
    N0 = 1/(np.exp(Eb_N0_dB[i]*np.log(10)/10.0))
    noise=np.random.normal(0,np.sqrt(N0/2.0),len(inter_data))
    rx=inter_data+noise
    tau=0
    delta=int(Tsym/2)
    center=60   # A r b i t a r y  r e c e i v e d  c e n t e r index
    #toff[i]=center%delta
    a=np.zeros(N)    
    avgsamples=6
    stepsize=1
    rit=-1
    GA=np.zeros(avgsamples)
    for k in range((delta),len(rx)-(delta),Tsym):
        #print k,
        rit=rit+1
        #b.append(rit)
        midsample=rx[center-1]
        latesample=rx[center+delta-1]
        earlysample=rx[center-delta-1]
        a[rit]=earlysample
        sub=latesample-earlysample
        GA[np.mod(rit,avgsamples)]=sub*midsample
        if (np.mean(GA)>0):
            tau=-stepsize
        else:
            tau=stepsize
        center=center+Tsym+tau
        if center>=len(rx)-delta:
            break;
    #print center
    #dum=np.fmod(center,delta)
    #poff[i]=dum
    xc=1*(a>0)
    error=(xc!=data).sum()
    BER_sim[i]=(1.0*error)/N 
    
theoryBer = 0.5*special.erfc(np.sqrt(10.0**(Eb_N0_dB/10.0)))    
plt.semilogy(Eb_N0_dB,theoryBer)    
plt.semilogy(Eb_N0_dB,BER_sim) 
plt.title("Timing Sync using Gardner TED")
plt.legend(['Theory','Simulated'],loc='best')
plt.xlabel('Eb/No (dB)')
plt.ylabel('$P_e$')
plt.grid(True)
plt.show()
