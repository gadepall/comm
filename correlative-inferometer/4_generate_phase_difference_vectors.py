import numpy as np
import matplotlib.pyplot as plt
import constantsForSetup as cs
from cmath import e,pi,sin,cos


M = cs.M
fc = cs.fc
fs = cs.fs
c = cs.c

phaseAngles = np.arange(180)*np.pi/180

#Distance from bteween two points
def findDistance(p1, p2):
    return np.linalg.norm(p1 - p2)

#function to find the phase difference between two vectors
def phiXY(vecX, vecY):
    return vecY/vecX

#get reciever antennae positions
def recieverPositions(M):
    positions = np.zeros([M, 2])
    radius = 1
    for iter in range(M):
        positions[iter, 0] = radius*np.cos(2*np.pi*iter/M)
        positions[iter, 1] = radius*np.sin(2*np.pi*iter/M)
    return positions

#Steering Vector as a function of theta and reciever positions
def a(theta, positions, M):
    radiusSource = 1000
    sourcePosition = np.array([radiusSource * np.cos(theta), radiusSource * np.sin(theta)])
    a1 = np.zeros(M, dtype = complex)
    for iter in range(M):
        a1[iter] = np.exp(-1j*2*pi*fc*findDistance(sourcePosition, positions[iter, :])/c)
    return a1

def getPhaseDifferenceVectors(theta, positions, M):
    steeringVectors = a(theta, positions, M)
    phaseDiffVectors = np.zeros(M, dtype = complex)
    for iter in range(M-1):
        phaseDiffVectors[iter] = phiXY(steeringVectors[iter], steeringVectors[iter+1])
    phaseDiffVectors[M-1] = phiXY(steeringVectors[M-1], steeringVectors[0])
    return phaseDiffVectors

phaseDiffVectors = np.zeros([180, M], dtype=complex)
phaseDiffVectorsIndex = 0

recieverPos = recieverPositions(M)

for iter in range(phaseAngles.shape[0]):
    phaseDiffVectors[iter, :] = getPhaseDifferenceVectors(phaseAngles[iter], recieverPos, M)

print("Shape of the phaseDiffVectors : ", phaseDiffVectors.shape)
np.save('phase_difference_vectors.npy', phaseDiffVectors)