# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 00:22:40 2019

@author: theresh
"""

import numpy as np
from alpha_tables import alpha_lookup_tables
from generator_polynomial import gen_poly
import kbch_nbch_selection
from syndromes_calc import syndromes
from index import index

def BCH_Decoder(code_rate,dxcm,N):
    kbch,nbch=kbch_nbch_selection.K_N(code_rate,N)
    alpha=alpha_lookup_tables(code_rate,N)
    g,Gg=gen_poly(N)
    m1,m=Gg.shape
    m=m-1
    n_bch=nbch #(2**(m))-1
    S,s=syndromes(code_rate,N,dxcm)    
    t=12
    
    ### B E R L E K A M P ' S   A L G O R I T H M
    e=np.zeros(nbch,dtype=int)
    lmd=np.zeros(t,dtype=int)
    T=np.zeros(t,dtype=int)
    lmd[0]=s[0]
    if s[0]==-1:
        T[0]=-1
        T[1]=0
    else:
        T[0]=np.mod((n_bch-s[0]),n_bch)
    for v in range(t-2):
        deltar=alpha[(s[2*v])%n_bch,:]
        for j in range(v):
            if lmd[j]==-1 | s[2*v-j]==-1:
                deltar=deltar
            else:
                deltar=np.mod(deltar+alpha[(lmd[j]+s[2*v-j])% n_bch,:],2)
        delta=index(deltar,code_rate,N)
        V=lmd
        if delta==-1|T[v]==-1:
            lmd[v+1]=-1
        else:
            lmd[v+1]=(delta+T[v])%n_bch
        
        for i in range(1,v):
            if delta==-1|T[i]==-1:
                lmdr=alpha[(lmd[i])%n_bch,:]
            else:
                lmdr=np.mod(alpha[lmd[i]%n_bch,:]+alpha[(T[i-1]+delta)% n_bch,:],2)                
                
            lmd[i]=index(lmdr,code_rate,N)
        if delta!=-1:
            T[0]=np.mod((n_bch-delta),n_bch)
            for i in range(1,v+1):
                T[i]=np.mod((V[i-1]-delta),n_bch)
        else:
           T[v+2]=T[v]
           for j in range(1,v+1):
               T[j]=0
    for i in range(nbch):
        xx=np.zeros(m,dtype=int)
        for j in range(t):
            if lmd[j]==-1:
                xx=xx
            else:
                xx=np.mod((xx+alpha[(lmd[j]+j*i)%n_bch,:]),2)
        if index(xx,code_rate,N)==1:
            e[np.mod(nbch-i,nbch)+1]=1
    
    d=np.mod(dxcm+e,2)
    return d
        
       
            
            
            

    
    
    
    
