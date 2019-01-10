# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:54:52 2017

@author: hemanth
"""

#convolutional decoder viterbi


import numpy as np
from numpy import linalg
from Prev_stage import prev_stage

def viterbi(y1,y2,N):
    distance=np.zeros((4,N+1))
    #initializing distances 
    distance[0:4,0]=[0,10e10,10e10,10e10]
    metric=np.zeros((8,N))
    
    for i in range(N):
        metric[0,i]=linalg.norm(np.array([-1,-1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 00 to 00
        metric[1,i]=linalg.norm(np.array([+1,+1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 00 to 10
        metric[2,i]=linalg.norm(np.array([-1,+1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 10 to 01    
        metric[3,i]=linalg.norm(np.array([+1,-1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 10 to 11
        metric[4,i]=linalg.norm(np.array([+1,+1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 01 to 00
        metric[5,i]=linalg.norm(np.array([-1,-1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 01 to 10
        metric[6,i]=linalg.norm(np.array([+1,-1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 11 to 01
        metric[7,i]=linalg.norm(np.array([-1,+1])-np.array([y1[i],y2[i]]))  #Mertic for transition from state 11 to 11
        
        distance[0,i+1]=np.min([distance[0,i]+metric[0,i],distance[2,i]+metric[4,i]]) #Minimum distance to reach state 00 at time i
        distance[1,i+1]=np.min([distance[0,i]+metric[1,i],distance[2,i]+metric[5,i]]) #Minimum distance to reach state 10 at time i
        distance[2,i+1]=np.min([distance[1,i]+metric[2,i],distance[3,i]+metric[6,i]]) #Minimum distance to reach state 01 at time i
        distance[3,i+1]=np.min([distance[1,i]+metric[3,i],distance[3,i]+metric[7,i]]) #Minimum distance to reach state 11 at time i
        
    state=np.argmin(distance[:,N])   #For the final stage pick the state corresponding to minimum weight
    #Starting from the final stage using the state, distances of previous stage and metric,
    #decoding the previous state and the corresponding Code bit
    decoded_bit_final=np.zeros((N,))
    for j in range(N-1,-1,-1):
        [state,decoded_bit]=prev_stage(state,distance[:,j],metric[:,j])
        decoded_bit_final[j]=decoded_bit #Storing the decoded bit in decode_bit_final vector
    return decoded_bit_final