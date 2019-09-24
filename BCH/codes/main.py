# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 01:31:07 2018

@author: theresh
"""

import numpy as np
import kbch_nbch_selection
from scipy import special
from Encoding import BCH_Encoder
from Decoding import BCH_Decoder
from matplotlib import pyplot as plt

N=64800
code_rate=np.divide(1,4.0)     # L D P C  R A T E 

kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)

Eb_N0_dB=np.linspace(0,2.5,6)

Eb=nbch/float(kbch)
ser=np.zeros(len(Eb_N0_dB))


for i in range(len(Eb_N0_dB)):
    N0 = Eb/(np.exp(Eb_N0_dB[i]*np.log(10)/10.0))   
    x=np.random.randint(0,2,kbch)  # G E N E R A T I N G   I N F O R M A T I O N  B I T S 
    #noise=(1/np.sqrt(2.0))*(np.random.normal(0,np.sqrt(N0/2.0),nbch)+1j*np.random.normal(0,np.sqrt(N0/2.0),nbch))
    noise=np.random.normal(0,np.sqrt(N0/2.0),nbch)
    x[0]=1
    c=BCH_Encoder(code_rate,x,N)        # E n c o d i n g  B i t s 
    xc=1-2*c  #B P S K  M o d u l a t i o n
    xcm=xc+noise  # R e c e i v e d  m a t r i x 
    dxcm=((xcm.real)<0)*1
    dxcm_decoding=BCH_Decoder(code_rate,dxcm,N)
    err=(dxcm_decoding[0:kbch]!=x[0:kbch]).sum()
    ser[i]=err/float(kbch)
    print err,
theoryBer = 0.5*special.erfc(np.sqrt(10.0**(Eb_N0_dB/10.0))) 
#plt.semilogy(Eb_N0_dB,ser,'-s',Eb_N0_dB,theoryBer,'r')
plt.semilogy(Eb_N0_dB,ser,'-s',linewidth=2)
plt.semilogy(Eb_N0_dB,theoryBer,'r')
plt.title("BCH ber curves in DVB-S2")
plt.legend(['Coded_BER','Uncoded_BER'],loc='best')
plt.xlabel('Eb/No (dB)')
plt.ylabel('Error Probability')
plt.grid(True)
plt.show()