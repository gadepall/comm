import numpy as np
import matplotlib.pyplot as plt
import constantsForSetup as cs
from cmath import e,pi,sin,cos

N = cs.N
M = cs.M
p = cs.p
fc = cs.fc
fs = cs.fs

#Generating Source Signal : Nxp

s = np.zeros((N,p),dtype=complex)
for t in np.arange(start=1,stop=p+1):
    t_val = t/fs
    s[:,t-1] = np.exp(1j*2*pi*fc*t_val)
print("Source Signal s : ",s.shape)

np.save('source_signal_data.npy',s)