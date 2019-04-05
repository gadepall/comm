# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:22:28 2019

@author: theresh
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import special

#=========================================================================================
# This program implemented based on the ""A BPSK/QPSK Timing-Error Detector for Sampled
# Receivers by FLOYD M.GARDNER,IEEE TRANSACTIONS ON COMMUNICATIONS, VOL.COM-34,NO. 5,
# MAY 1986"". This is a simple algorithm for detection of timing error of a synchronous,
# bandlimited, BPSK or QPSK datastrem. The algorithm requires two samples for symbol. And
# uses one of the two samples for the Symbol decision. It's purely a non data aided Timing
# Error detection.
#=========================================================================================



#=========================================================================================
# Inputs : 1) Simulation Length (N) (Total number of symbols)
#	   2) Samples per Symbol (M)
#          3) Eb_N0_dB Range
#          4) Length_Prev_Symbols (For averange purpose)
#
# Output : 1) BER_sim

# Plot : BER Curve for theorical simulation vs Algorithm             
#==========================================================================================


#==========================================================================================
#Transmitter
#==========================================================================================
N=100000   # Simulation length
data=np.random.randint(0,2,N) # Generation of random bits
c=2*data-1   # BPSK mapping
M=100     # Number of samples per symbol.
p=np.ones(M)            # shape Pulse shape
Mapped_Data=np.zeros(N*M) # Total samples
for i in range(N):
    Mapped_Data[i*M:(i+1)*M]=c[i]  # Interpolated BPSK data using the pulse shaping filter(NRZ)
#==========================================================================================

Eb_N0_dB=np.linspace(0,10,11) # SNR range in dB scale
len_eb_n0=len(Eb_N0_dB)        
time_offsets=np.array([3,30,95])  # List of Timing Offsets
len_time_offsets=len(time_offsets)
BER_sim=np.zeros((len_time_offsets,len_eb_n0))   # Bit Error Rate Values

for off in range(len_time_offsets):
    for i in range(len_eb_n0):
        #========================================================
        # Noise characteristics
        N0 = 1/(np.exp(Eb_N0_dB[i]*np.log(10)/10.0))
        noise=np.random.normal(0,np.sqrt(N0/2.0),len(Mapped_Data)) 
        #=========================================================
        #=========================================================

        rx=Mapped_Data+noise   # Noisy received samples
        delta=M/2  # Actual Mid sample index. 
        timing_offset=time_offsets[off]  # Timing offset addition 
        center=delta + timing_offset  # New center.
    
        #===========================================================
        # Gardner TED algorithm
        #===========================================================
        Decision_Samples=np.zeros(N)    # Samples storing for making Decision. (DS).   
        Length_Prev_Symbols=6     # User Specified Le: Used for the Averaging Purpose
        Prev_Samples=np.zeros(Length_Prev_Symbols)
        increment=1
        index_DS=-1     # Index of Decision samples while storing the data.
        tau=0
        for k in range((delta),len(rx)-(delta),M):
            index_DS=index_DS+1
            m_s=rx[center-1]    # Middle sample
            l_s=rx[center+delta-1] # Late sample
            e_s=rx[center-delta-1] # Early sample
            Decision_Samples[index_DS]=e_s  # As per the algorithm.
            sub=l_s-e_s
            Prev_Samples[np.mod(index_DS,Length_Prev_Symbols)]=sub*m_s  # Algorithm specified
            if (np.mean(Prev_Samples)>0):
                tau=-increment
            else:
                tau=increment
            center=center+M+tau
            if center>=len(rx)-delta:  # Breaking Statement
                break;
        #===============================================================
        # Decision and Bit Error Rate Calulation
        xc=1*(Decision_Samples>0)
        error=(xc!=data).sum()
        BER_sim[off][i]=(1.0*error)/N 
        #=================================================================



#============================================================================================
#Theoritical BER for BPSK
theoryBer = 0.5*special.erfc(np.sqrt(10.0**(Eb_N0_dB/10.0)))    
#============================================================================================


#============================================================================================
# Plotting the data
plt.semilogy(Eb_N0_dB,theoryBer,'y')    
plt.semilogy(Eb_N0_dB,BER_sim[0],'b',Eb_N0_dB,BER_sim[1],'g',Eb_N0_dB,BER_sim[2],'r') 
plt.title("Timing Sync using Gardner TED")
plt.legend(['$\\tau=0$','$\\tau=%d$'%time_offsets[0],'$\\tau=%d$'%time_offsets[1],'$\\tau=%d$'%time_offsets[2]],loc='best')
plt.xlabel('$\\frac{Eb}{N0}$(dB)')
plt.ylabel('$P_e$')
plt.grid(True)
plt.savefig("./Different_timeoffsets_snrvsber.eps")
plt.show()
#=============================================================================================
