import numpy as np
import matplotlib.pyplot as plt
import math
import random
def qfunc(x):
	return 0.5*math.erfc(x/math.sqrt(2))
snr_db = np.linspace(0,9,10)
snr = 10**(0.1*snr_db)
err_sim = []

err_ana = []
bits = []
bits = np.random.randint(0,2,100)


for i in range(0,len(snr)):
    t = 0
    r = []
    
        
    for j in range(0,len(bits)):
        n1 = np.random.normal(0,1,1)
        rx = (math.sqrt(snr[i]))*(1-2*bits[j]) + n1
        if(rx>=0):
            r.append(0)

        else:
            r.append(1)

    for k in range(0,len(bits)):
        if(bits[k]!=r[k]):
            t = t+1;
    err_sim.append(t/100)
    err_ana.append(qfunc(math.sqrt(snr[i])))
plt.semilogy(snr_db.T,err_ana,label='Analysis')
plt.semilogy(snr_db.T,err_sim,'o',label='Sim')
plt.xlabel('SNR$\\left(\\frac{E_b}{N_o}\\right)$')
plt.ylabel('$P_e$')
plt.legend()
plt.grid()
#if using termux
plt.savefig('./figs/ee18btech11042/ee18btech11042.pdf')
plt.savefig('./figs/ee18btech11042/ee18btech11042_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11042/ee18btech11042.pdf"))
#else
#plt.show()
plt.show()
	

    
             
