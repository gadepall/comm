# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 08:51:42 2017

@author: hemanth
"""
#Starts from the current decoded state, takes input as minimum distance to
#reach that state and previous state And returns previous state and decoded
#information bit corresponding to that state.


import numpy as np

def prev_stage(curr_state,distance_prev,metric):
    
    if(curr_state==0):
        if(distance_prev[0]+metric[0] <= distance_prev[2]+metric[4]):
            prev_state=0
            decoded_bit=0
        else:
            prev_state=2
            decoded_bit=0
    
    elif(curr_state==1):
        if(distance_prev[0]+metric[1] <= distance_prev[2]+metric[5]):
            prev_state=0
            decoded_bit=1
        else:
            prev_state=2
            decoded_bit=1
    elif(curr_state==2):
        if(distance_prev[1]+metric[2] <= distance_prev[3]+metric[6]):
            prev_state=1
            decoded_bit=0
        else:
            prev_state=3
            decoded_bit=0
    elif(curr_state==3):
        if(distance_prev[1]+metric[3] <= distance_prev[3]+metric[7]):
            prev_state=1
            decoded_bit=1
        else:
            prev_state=3
            decoded_bit=1
    return prev_state,decoded_bit
        
    
        