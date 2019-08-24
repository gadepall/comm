import numpy as np
import matplotlib.pyplot as plt
import constantsForSetup as cs
from cmath import e,pi,sin,cos

N = cs.N
M = cs.M
p = cs.p
fc = cs.fc
fs = cs.fs

#get positions of the recievers
def recieverPositions(M):
    positions = np.zeros([M, 2])
    radius = 1
    for iter in range(M):
        positions[iter, 0] = radius*np.cos(2*np.pi*iter/M)
        positions[iter, 1] = radius*np.sin(2*np.pi*iter/M)
    return positions


#source data
s = np.load('source_signal_data.npy')
print("Source Signal s : ",s.shape)

#storing DOAs in radians
doa = cs.doaInDegrees*pi/180
print("Original Directions of Arrival (degrees): \n",doa*180/pi)


c = cs.c

#Distance from bteween two points
def findDistance(p1, p2):
    return np.linalg.norm(p1 - p2)

#Steering Vector as a function of theta and position
def a(theta, positions, M):
    radiusSource = 1000
    sourcePosition = np.array([radiusSource * np.cos(theta), radiusSource * np.sin(theta)])
    a1 = np.zeros(M, dtype = complex)
    for iter in range(M):
        a1[iter] = np.exp(-1j*2*pi*fc*findDistance(sourcePosition, positions[iter, :])/c)
    return a1

A = np.zeros((M,N),dtype=complex)
recieverPos = recieverPositions(M)
for i in range(N):
    A[:,i] = a(doa[i], recieverPos, M)[:]
print("Steering Matrix A: ",A.shape)


#Generating Recieved Signal
noise = np.random.multivariate_normal(mean=np.zeros(M),cov=np.diag(np.ones(M)),size=p).T
X = (A@s + noise)
print("Recieved Signal X: ",X.shape)


np.save('recieved_signal_data.npy', X)