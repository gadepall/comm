import numpy as np


def qpsk1(N,mx):
	x_mapping=np.zeros(len(x)/2,dtype=complex)
	i=0
	k=0
	while(i<len(x)):
	    if mx[i]==1 and mx[i+1]==1:
	        x_mapping[k]=complex(1,1)
	    elif mx[i]==1 and mx[i+1]==-1:
	        x_mapping[k]=complex(1,-1)
	    elif mx[i]==-1 and mx[i+1]==1:
	        x_mapping[k]=complex(-1,1)
	    elif mx[i]==-1 and mx[i+1]==-1:
	        x_mapping[k]=complex(-1,-1)     
	    i=i+2
	    k=k+1
	x_mapping1=np.divide(x_mapping,np.sqrt(2))
	qpsk = x_mapping1
	return qpsk
 
def pilot():
    sof=np.array([0,1,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0])  #18D2E82 : SOF OF DVBS2
    g1=np.array([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
    g2=np.array([0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1])
    g3=np.array([0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1])
    g4=np.array([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1])
    g5=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    g6=np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    G=np.vstack((g1,g2,g3,g4,g5,g6))
    modcod=np.array([0,0,1,0,0,0,1])
    modcod=modcod.T
    dum=np.matmul(modcod[0:6],G)
    dum1=np.zeros(64,dtype=int)
    k = 0
    for i in range(32):
        dum1[k]=dum[i]
        k+=1
        dum1[k]=modcod[6]^dum[i]
        k+=1
                
    plsc=np.array([0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1
                    ,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0])
    plsc=(plsc+dum1)%2
    plheader=np.hstack((sof,plsc))
    return plheader
 
N=64800
x=np.random.randint(0,2,N)
#print x.shape
mx=np.subtract(np.multiply(x,2),1)
#print mx.shape
qpsk = qpsk1(N,mx)
plheader=pilot()

xpilots=np.zeros(90,dtype=complex)
for i in range(45):
    x1=(1/np.sqrt(2))*(1-2*plheader[2*i+1]) 
    xpilots[2*i+1]=np.complex(x1,x1)
    x2=-1*(1/np.sqrt(2))*(1-2*plheader[2*i]) 
    xpilots[2*i]=np.complex(x2,-x2)

def insertpilot(final, i, P):
    for k in range(0,36):
        final[i] = P[k]
        i+=1
    return final,i

P=np.complex(np.sqrt(1.0/2),np.sqrt(1.0/2))*np.ones(36,dtype=complex)

fin = np.zeros(33192,dtype = complex)
j = 0
l = 0
m = 0
print fin.shape
print qpsk.shape
for i in range (0,32400):
    if (i%1440==0 and i!= 0):
        fin , m = insertpilot(fin, m, P)
    fin[m] = qpsk[j]
    j+=1
    m+=1
final = np.hstack((xpilots,fin))
print final.shape
Eb_N0_dB=-3
n0 = 10**(-Eb_N0_dB/10.0)
noise=np.random.normal(0,np.sqrt(n0/2),len(final))+1j*np.random.normal(0,np.sqrt(n0/2),len(final))

phase=np.exp(np.complex(0,1)*(np.pi/2.5))
rx=phase*final+noise
