# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 08:45:25 2017

@author: hemanth
"""
#conv_in shoud be list
#convolution encoder
def conv_Encoder(conv_in):

 #intial shift register values
    m1=0
    m2=0
    m3=0
    len_msg=len(conv_in)
    conv_out=[]

    for i in range(len_msg):
        m1=conv_in[i]
        x1=m1^m3
        x2=m1^m2^m3 
        conv_out.append(x1)
        conv_out.append(x2)
        m3=m2
        m2=m1
    return conv_out