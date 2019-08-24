
import numpy as np
import matplotlib.pyplot as plt
import constantsForSetup as cs
from cmath import e,pi,sin,cos

N=cs.N
M=cs.M
p=cs.p
fc=cs.fc
fs=cs.fs
c = cs.c

#calculate phase difference vectors
def calcPhaseDiffVectors(X, M):
    phaseDiffVectors = np.zeros(M, dtype = complex)
    for iter in range(M-1):
        phaseDiffVectors[iter] = phiXY(X[iter, :], X[iter+1, :])
    phaseDiffVectors[M-1] = phiXY(X[M-1, :], X[0, :])
    return phaseDiffVectors

#function to correlate two given phase difference vectors
def correlatePhaseDiffVectors(vecX, vecY):
    return np.abs(np.matmul(vecX.conjugate(), vecY)/(np.linalg.norm(vecX) * np.linalg.norm(vecY)))

#function to find the phase difference between two vectors
def phiXY(vecX, vecY):
    return (np.matmul(vecX.conjugate(), vecY)/(np.linalg.norm(vecX) * np.linalg.norm(vecY)))

#function to find the nC2 for a given n
def nc2(n):
    return int(n*(n-1)/2)

#reference phase difference vectors
phiR = np.load('phase_difference_vectors.npy')
#print(phiR)

#recieved signal data
X = np.load('recieved_signal_data.npy')
print("Recieved Signal X: ",X.shape)

#calculate phase difference vectors
calculatedPhaseDiffVector = calcPhaseDiffVectors(X, M)

print("Shape of phase difference vectors : ", calculatedPhaseDiffVector.shape)
#calculate correlation with the reference data
correlationValues = np.zeros(phiR.shape[0])
print("Shape of phase reference vectors : ", phiR.shape)

print(phiR.shape[0])
for iter in range(phiR.shape[0]):
    correlationValues[iter] = correlatePhaseDiffVectors(calculatedPhaseDiffVector, phiR[iter, :])
#plotting original DOAs for comparison with peaks
fig, ax = plt.subplots(figsize=(10,4))
doa = cs.doaInDegrees
print("Original Directions of Arrival (degrees): \n",doa)
for k in range(len(doa)):
	plt.axvline(x=doa[k],color='red',linestyle='--')

#Plotting P_vals vs theta to find peaks
theta_vals = np.arange(0,180,1)

plt.plot(np.abs(theta_vals), correlationValues)
plt.xticks(np.arange(0, 180, 10))
plt.xlabel('$\\theta$')
plt.ylabel('$P(\\theta)$')
plt.title('Dotted Lines = Actual DOA    Peaks = Estimated DOA')

plt.legend()
plt.grid()
#else
plt.show()
