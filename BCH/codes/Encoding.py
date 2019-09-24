# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 15:02:39 2019

@author: theresh
"""

import numpy as np
from generator_polynomial import gen_poly
import kbch_nbch_selection

def magic (numbers):
    return int (''.join(["%d"%x for x in numbers]))
def xor(a,b):
    result=[]
    for i in range(1,len(b)):
        if a[i]==b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)


def mod2div(divident,divisor):
    pick=len(divisor)
    tmp=divident[0:pick]
    while pick <len(divident):
        if tmp[0]=='1':
            tmp=xor(divisor,tmp)+divident[pick]
        else:
            tmp=xor('0'*pick,tmp)+divident[pick]

        pick+=1

    if tmp[0] =='1':
        tmp=xor(divisor,tmp)
       # print("temp1 is",tmp)
    else:
        tmp=xor('0'*pick,tmp)
        #print("temp2 is ",tmp)

    checkword=tmp
    return checkword
def encodeData(data,key):
    appended_data=data
    remainder=mod2div(appended_data,key)
    return remainder


def BCH_Encoder(code_rate,x,N):
    kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)
    g,Gg=gen_poly(N)
    g=g%2
    m=np.concatenate((x,np.zeros(nbch-kbch,dtype=int)))
    m=str(magic(m))
    g=str(magic(g))
#
    encoded_data=encodeData(m,g)
    m=[int (i) for i in str(m)]
    m=np.array(m)
    parity_bits=[int (i) for i in str(encoded_data)]
    parity_bits=np.array(parity_bits)

    m[kbch:,]=parity_bits

    return m