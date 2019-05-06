#in this code is generalised only the qpsk_bits and noise...please check and if possible do modifications...it would be great help.

import numpy as np 
import matplotlib.pyplot as plt 
import scipy

def qpsk1(x, size):
	qpsk =[]
	for i in range(0,size,2):
		if x[i]==0 and x[i]==0:
			qpsk.append(complex(1,1))
		elif x[i]==0 and x[i]==1:
			qpsk.append(complex(-1,1))
		elif x[i]==1 and x[i]==0:
			qpsk.append(complex(-1,-1))
		else:
			qpsk.append(complex(1,-1))

	for i in range(size/2):
		qpsk[i]= qpsk[i]/np.sqrt(2)

	return qpsk

def pulse(alpha):

    os = 8

    t = np.linspace(-4,4,os*(4+4)+1)

    p = [0]*65

    for i in range(0,len(t)):

        if t[i]==0:

            p[i] = (1-alpha)+4*alpha/np.pi

        elif t[i] == 1/(4*alpha):

            p[i] = (alpha/(np.sqrt(2)))*((1+2/np.pi)*np.sin(np.pi/(4*alpha))+ (1-2/np.pi)*np.cos(np.pi/(4*alpha)))

        elif t[i] == -1/(4*alpha):

            p[i] = (alpha/(np.sqrt(2)))*((1+2/np.pi)*np.sin(np.pi/(4*alpha))+ (1-2/np.pi)*np.cos(np.pi/(4*alpha)))

        else:

            p[i] = (np.sin(np.pi*t[i]*(1-alpha))+ 4*alpha*t[i]*np.cos(np.pi*t[i]*(1+alpha)))/(np.pi*t[i]*(1-(4*alpha*t[i])**2))

    sum = 0

    for i in range(0,len(t)):

        sum = sum + p[i]**2



    for i in range(0,len(t)):

        p[i] = p[i]/np.sqrt(sum)           

    return p

alpha = [0.2,0.25,0.35]

final = []

for i in range(0,len(alpha)):
	
	os = 8
	t = np.linspace(-4,4,os*(4+4)+1)

	p = pulse(alpha[i])

	def ber(numbits,snrdb):
		num_bits = int(numbits)
		bits = np.random.randint(2, size = 2*num_bits)
		qpsk_bits = qpsk1(bits, 2*num_bits)  # qpsk symbols generation


		os = 8
		bits_os = []
		for i in range(0,num_bits):
			bits_os.append(qpsk_bits[i])
			for j in range(0,os-1):
				bits_os.append(0)
		output_of_srrc_filterr = np.convolve(bits_os, p)  # pulse shaping
		# noise = np.random.normal(0,np.sqrt(10**(-snrdb*0.1)),len(output_of_srrc_filterr))


		noise = scipy.vectorize(complex)
		noise = noise((np.random.normal(0,np.sqrt(10**(-snrdb*0.1)),len(output_of_srrc_filterr)))/np.sqrt(2) , (np.random.normal(0,np.sqrt(10**(-snrdb*0.1)),len(output_of_srrc_filterr)))/np.sqrt(2))

		for i in range(0,len(output_of_srrc_filterr)):
			output_of_srrc_filterr[i] = output_of_srrc_filterr[i]+noise[i]
		y = np.convolve(output_of_srrc_filterr,p)                                # matched filtering
		y_truncated = y[len(t)-1:len(y)]      #This number 65 will change is oversampling rate is changed 
		y_down = []
		for i in range(0,num_bits):
			y_down.append(y_truncated[0+8*i])
		bits_hat = []     # recovered bits.
		difference = 0
		# for i in range(0, num_bits):
		# 	if (y_down[i]>0 and bits[i]==0 ) or (y_down[i]<0 and bits[i]==1 ) :
		# 		difference = difference+1

		for i in range(len(y_down)):
			var = np.angle(y_down[i])

			if var>=0 and var<np.pi/2:
				bits_hat.append(complex(1,1))
			elif var>=np.pi/2 and var<np.pi:
				bits_hat.append(complex(-1,1))
			elif var>=-np.pi and var<(-1*np.pi)/2:
				bits_hat.append(complex(-1,-1))
			elif var>=(-1*np.pi)/2 and var<0:
				bits_hat.append(complex(1,-1))   # decoding part

			bits_hat[i] = bits_hat[i]/np.sqrt(2)



		for i in range(0, num_bits):
			if bits_hat[i] != qpsk_bits[i]:
				difference = difference+1

		#print "bits="+str(num_bits)+"	snrdb="+str(snrdb)+"	difference="+str(difference)

		
		return difference/(1.0*num_bits)



	


			
	snrdb = np.linspace(0,15,16)
	num_bits = 64800
	vecber = scipy.vectorize(ber)
	
	final.append(vecber( num_bits,snrdb  ))

	# plt.semilogy(snrdb,vecber( num_bits,snrdb  ),'r' )
	# plt.semilogy(snrdb, vecdemodulate(num_bits,snrdb))
	# plt.xlabel('$\\frac{E_b}{N_0}$(dB)')
	# plt.ylabel('$P_e$')	
	# plt.legend(loc='best')
	# plt.grid()
	# plt.show()

def demodulate_qpsk(num_bits,snrdb):
		num_bits = int(num_bits)
		bits = np.random.randint(2, size = 2*num_bits)
		qpsk_bits1 = qpsk1(bits, 2*num_bits)  # qpsk symbols generation
		noise = scipy.vectorize(complex)
		noise = noise((np.random.normal(0,np.sqrt(10**(-snrdb*0.1)),num_bits))/np.sqrt(2) , (np.random.normal(0,np.sqrt(10**(-snrdb*0.1)),num_bits))/np.sqrt(2))
		qpsk_bits = qpsk_bits1 + noise
		bits_hat = []
		for i in range(len(qpsk_bits)):
			var = np.angle(qpsk_bits[i])

			if var>=0 and var<np.pi/2:
				bits_hat.append(complex(1,1))
			elif var>=np.pi/2 and var<np.pi:
				bits_hat.append(complex(-1,1))
			elif var>=-np.pi and var<(-1*np.pi)/2:
				bits_hat.append(complex(-1,-1))
			elif var>=(-1*np.pi)/2 and var<0:
				bits_hat.append(complex(1,-1))   # decoding part

			bits_hat[i] = bits_hat[i]/np.sqrt(2)

		difference =0

		for i in range(0, num_bits):
			if bits_hat[i] != qpsk_bits1[i]:
				difference = difference+1

		return difference/(1.0*num_bits)


snrdb = np.linspace(0,15,16)
num_bits = int(64800)

vecdemodulate = scipy.vectorize(demodulate_qpsk)
plt.semilogy(snrdb, vecdemodulate(num_bits,snrdb), 'o')
plt.semilogy(snrdb,final[0])
plt.semilogy(snrdb,final[1])
plt.semilogy(snrdb,final[2])
plt.xlabel('$\\frac{E_b}{N_0}$(dB)')
plt.ylabel('$P_e$')	
plt.legend(['Without Pulse Shaping','$\\alpha = %0.2f$'%alpha[0],'$\\alpha = %0.2f$'%alpha[1],'$\\alpha = %0.2f$'%alpha[2]],loc='best')
plt.grid(True)
plt.savefig("./pulseshaping.eps")
plt.show()
