# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:53:53 2019

@author: theresh
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import special
#If using termux
import subprocess
import shlex
#end if

N=10**4
data=np.random.randint(0,2,N)
c=2*data-1
Tsym=100
sym_samp=np.arange(0,100)
Eb_N0_dB=np.linspace(0,5,6)
BER_sim=np.zeros(len(Eb_N0_dB))
MSE=np.zeros(len(Eb_N0_dB))
pulse=np.sin(2*np.pi*sym_samp/(2*Tsym))
inter_data=np.zeros(N*Tsym)
for i in range(N):
    inter_data[i*Tsym]=c[i]
w=np.convolve(inter_data,pulse)

for i in range(len(Eb_N0_dB)):
    N0 = 1/(np.exp(Eb_N0_dB[i]*np.log(10)/10.0))
    noise=np.random.normal(0,np.sqrt(N0/2.0),len(w))
    rx=w+noise
    tau=0
    delta=int(Tsym/2)
    center=60
    a=np.zeros(N)
    cenpoint=np.zeros(N)
    remind=np.zeros(N)
    avgsamples=10
    stepsize=1
    rit=-1
    GA=np.zeros(avgsamples)
    #tauvector=np.zeros(1900)
    uor=-1
    for k in range((delta),len(rx)-(delta),Tsym):
        #print k,
        rit=rit+1
        #b.append(rit)
        midsample=rx[center-1]
        latesample=rx[center+delta-1]
        earlysample=rx[center-delta-1]
        a[rit]=earlysample
        sub=latesample-earlysample
        #print np.fmod(rit,avgsamples)
        GA[np.fmod(rit,avgsamples)]=sub*midsample
        #print GA
        if (np.mean(GA)>0):
            tau=-stepsize
        else:
            tau=stepsize
        cenpoint[rit]=center
        remind[rit]=(center-delta)%Tsym
#        if rit>=100 and rit<2000:
#            uor=uor+1
#            tauvector[uor]=(remind[rit-delta])**2
        center=center+Tsym+tau
        if center>=len(rx)-delta:
            break;
    #MSE[i]=np.mean(tauvector)
#    symbols=200
#    plt.subplot(3,1,1)
#    plt.plot(remind[0:symbols])
#    lim1=40*np.ones(symbols)
#    lim2=60*np.ones(symbols)
#    plt.plot(lim1)
#    plt.plot(lim2)
#    plt.title('Convergenece plot for BPSK using Gardner TED')
#    plt.ylabel('tau axis')
#    plt.xlabel('iterations')
    symbols=2000
    plt.subplot(2,1,1)
    plt.plot(remind[0:symbols])
    lim1=40*np.ones(symbols)
    lim2=60*np.ones(symbols)
    plt.plot(lim1)
    plt.plot(lim2) 
    plt.title('Convergenece plot for BPSK using Gardner TED')
    plt.ylabel('$\\tau$')
    plt.xlabel('iterations')    
    xc=1*(a>0)
    error=(xc!=data).sum()
    BER_sim[i]=(1.0*error)/N 
    
theoryBer = 0.5*special.erfc(np.sqrt(10.0**(Eb_N0_dB/10.0)))    
plt.subplot(2,1,2)    
plt.semilogy(Eb_N0_dB,theoryBer)    
plt.semilogy(Eb_N0_dB,BER_sim) 
#plt.title("Timing Sync using Gardner TED")
plt.legend(['Theory','Simulated'],loc='best')
plt.xlabel('Eb/No (dB)')
plt.ylabel('BER')
plt.grid(True)

#If using termux
plt.savefig('../figs/time_ber.pdf')
plt.savefig('../figs/time_ber.eps')
subprocess.run(shlex.split("termux-open ../figs/time_ber.pdf"))
#else
#plt.show()

