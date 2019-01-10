# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:48:59 2017

@author: hemanth
"""

import numpy as np
from scipy import special
from conv_encoder import conv_Encoder
from Viterbi_decoder import viterbi
import matplotlib.pyplot as plt

N=int(2e6)

Eb_N0_dB=np.arange(0,11,1)

Ec_N0_dB=Eb_N0_dB - 10*np.log10(2.0/1.0)

snrlen=11

nErr_hard=np.zeros((1,11))

for i in range(snrlen):
    ip = np.random.randint(2,size=N) #generating 0,1 with equa probability
    conv_in=list(ip)


    conv_in[N-1]=0
    conv_in[N-2]=0
    conv_out=conv_Encoder(conv_in) #convoution encoder


    conv1_out=conv_out[0:len(conv_out):2]
    conv2_out=conv_out[1:len(conv_out):2]

    conv1_mod=2*np.array(conv1_out)-1
    conv2_mod=2*np.array(conv2_out)-1

    #noise

    sigma = np.sqrt((1/2.0)*(10**(-Ec_N0_dB[i]/10.0)))
    n1=np.random.normal(0,sigma,(np.shape(conv1_out)))  
    n2=np.random.normal(0,sigma,(np.shape(conv2_out)))  

    #adding noise
    y1=conv1_mod+n1
    y2=conv2_mod+n2


    decoded_bits=viterbi(y1,y2,N)
    
    
    nErr_hard[0,i] = np.count_nonzero(decoded_bits-conv_in)  



theoryBer = 0.5*special.erfc(np.sqrt(10**(Eb_N0_dB/10.0))) # theoretical ber uncoded AWGN
simBer_hard    = nErr_hard/float(N)

plt.plot(Eb_N0_dB,theoryBer,'b',Eb_N0_dB,simBer_hard[0],'g')
plt.legend(['theory-Uncoded','coded-hard'],loc=1)
plt.yscale('log')
plt.ylabel('Bit Error Rate')
plt.xlabel('Eb/N0 in dB')
plt.title('BER for BPSK in AWGN with rate 1/2 convoution code')
#plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11])
plt.grid()


plt.show()