# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 00:52:15 2017

@author: hemanth
"""
import numpy as np
from scipy import special
import matplotlib.pyplot as plt


N=2*(10**6)  #number of bits

Eb_N0_dB=np.arange(0,11,1)

Ec_N0_dB=Eb_N0_dB - 10*np.log10(7.0/4)

ht=np.matrix([[1,0,1],[1,1,1],[1,1,0],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])

g=np.matrix([ [1,0,0,0,1,0,1],[0,1,0,0,1,1,1],[0,0,1,0,1,1,0],[0,0,0,1,0,1,1]])

bitIdx = [7,7,4,7,1,3,2]

c_vec = np.zeros((2**4,7))

nErr_hard=np.zeros((1,11))

nErr_soft=np.zeros((1,11))

#Encoder

for kk in range(2**4):
    m_vec=np.matrix(map(int,np.binary_repr(kk,width=4)))
    c_vec[kk,:]=(m_vec*g)%2

 
for yy in range(len(Eb_N0_dB)): 
    
    #trasmitter
    ip = np.random.randint(2,size=N) #generating 0,1 with equa probability
    
    ip=np.array(ip)
        #hamming coding (7,4)
    ipM=np.matrix(np.reshape(ip,(-1,4)))
    ipC=(ipM*g)%2
    cip=np.reshape(ipC,(1,(N/4)*7))
        
        #modulation
    s=2*cip-1     #BPSK modulation 0 -> -1; 1 -> 0
        
        #channel-AWGN
        
   # N0 = 1/(np.exp(Ec_N0_dB[yy]*np.log(10)/10)) 
    sigma = np.sqrt((1/2.0)*(10**(-Ec_N0_dB[yy]/10)))
    n=np.random.normal(0,sigma,(np.shape(cip)))
         
        #noise addition
    y=s+n
   
    y=np.array(y) 
       #receiver
    cipHard=(y>0)*1
        
        #hard decision hamming decoder
    cipHardM = np.matrix(np.reshape(cipHard,(-1,7)))
    syndrome = (cipHardM*ht)%2
    syndrome = np.array(syndrome).astype(int)
    a=np.array([[4,2,1]])
    a=np.reshape(np.tile(a,N/4),(N/4,3))
    
    syndromeDec =np.sum(syndrome*a,axis=1)
    #    
    syndromeDec[syndromeDec==0]=1
    bitIdx=np.array(bitIdx)
    bitCorrIdx  = bitIdx[syndromeDec-1] # find the bits to correct
    bitCorrIdx  = bitCorrIdx + np.arange(0,N/4,1)*7  # finding the index in the array
    cipHard[0,bitCorrIdx-1] = 1-cipHard[0,bitCorrIdx-1]  # correcting bits
    a1=np.arange(1,5,1)
    a1=np.tile(a1,N/4)
    b1=np.repeat(np.arange(0,N/4)*7,4)
    idx =a1+b1   # index of data bits
    ipHat_hard = cipHard[0,idx-1]  # selecting data bits
    
    #    Soft decision Hamming decoder
    cipSoftM    = np.reshape(np.real(y),(-1,7))
    c_vec=np.matrix(c_vec)
    corr=cipSoftM*(2*c_vec.T-1)
    idx=corr.argmax(axis=1)
    ipHat_soft=[]
    for i1 in range(np.shape(idx)[0]):
        aa=list(np.binary_repr(idx[i1,0],width=4))
        for j1 in range(4):
            ipHat_soft.append(int(aa[j1]))
    ipHat_soft =np.array(ipHat_soft)
       
    #    counting the errors
     
    nErr_hard[0,yy] = np.count_nonzero(ip-ipHat_hard)   
    nErr_soft[0,yy] = np.count_nonzero(ip-ipHat_soft)   
    
theoryBer = 0.5*special.erfc(np.sqrt(10**(Eb_N0_dB/10.0))) # theoretical ber uncoded AWGN
simBer_hard    = nErr_hard/float(N)
simBer_soft    = nErr_soft/float(N)

#plt.plot(Eb_N0_dB, theoryBer, marker='*', linestyle='-', color='b', label='theory-Uncoded')
#plt.plot(Eb_N0_dB, simBer_hard, marker='*', linestyle='-', color='r', label='coded-hard decision')
#plt.plot(Eb_N0_dB, simBer_soft, marker='*', linestyle='-', color='p', label='coded-soft decision')
plt.plot(Eb_N0_dB,theoryBer,'b',Eb_N0_dB,simBer_hard[0],'r',Eb_N0_dB,simBer_soft[0],'g')
plt.legend(['theory-Uncoded','coded-hard','coded-soft'],loc=1)
plt.yscale('log')
plt.ylabel('Bit Error Rate')
plt.xlabel('Eb/N0 in dB')
plt.title('BER for BPSK in AWGN with hamming(7,4) code')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11])
plt.grid()


#plt.show()

