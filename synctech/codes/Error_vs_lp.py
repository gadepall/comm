import numpy as np 
import matplotlib.pyplot as plt 
import cmath
import scipy


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

def saw(x):
	x = float(x)
	if x<np.pi and x>=(-np.pi):
		return x
	else: 
		x = x%(2*np.pi)
		if x>np.pi:
			x = x - 2*np.pi
		return x


N=200000
x=np.random.randint(0,2,N)
mx=np.subtract(np.multiply(x,2),1)
qpsk = qpsk1(N,mx)
#print qpsk.shape
lp = 36
es = 1
n0 = np.sqrt(0.5*(10.0**(-1/10.0)))
sigma = 1.0/(2*lp*lp*es/n0)
noise=np.random.normal(0,sigma,N/2)+1j*np.random.normal(0,sigma,N/2)
phi = saw(np.random.rand(1))
#print phi.shape
v = scipy.vectorize(complex)
r = np.exp(v(np.zeros(int(N/2)),phi)) 
#print noise.shape
received = qpsk*r + noise
snr = np.sqrt((qpsk*r/noise)*np.conj((qpsk*r/noise))) 
#print snr
#print received.shape

############### Applying First step of the algorithm ###############################
k = 0
r = scipy.vectorize(complex)
theta_hat = np.zeros([lp,])
for i in range(0,lp):
	theta_hat1 = received[i]*np.conj(qpsk[i])
	theta_hat[i] = cmath.phase(theta_hat1)


############### Applying Second step of the algorithm ##############################

alpha = 0.5
theta = np.zeros([lp,])
for i in range(1,theta_hat.shape[0]):
	theta[i] = theta[i-1] + alpha*saw(theta_hat[i]-theta[i-1])

phi_m = np.zeros(theta.shape)
phi_m[0:] = phi
theta1 = (phi_m-theta)**2
x1 = np.linspace(0,theta1.shape[0],theta1.shape[0])
plt.plot(x1,theta1)
plt.xlabel('$No$ $of$ $Pilots$')
plt.ylabel('$Squared$ $phase$ $error$')
plt.grid()
plt.show()