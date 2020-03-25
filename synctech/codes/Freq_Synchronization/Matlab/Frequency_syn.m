clc;
clear all;
close all;

variance = 1;
simlen = 18;
Ts = 1e-9;
theta = 0;
v=zeros(simlen,1)+1j*zeros(simlen,1);
V=randn(simlen,1)+1j*randn(simlen,1);
%V=zeros(simlen,1)+1j*zeros(simlen,1);
k=transpose(linspace(1,simlen,simlen));
A=transpose(linspace(1,5,simlen));
estimate=zeros(length(A),1);
for kk=1:length(A)
delf=5e6;
r1=zeros(simlen,1)+1j*(2*pi*delf*(k-1)*Ts+theta);
r=A(kk).*exp(r1)+V;
M=18;
fnm=0;
fdm=0;
for i=0:M-1
    tot=0;
    for j=i+1:simlen
        tot=tot+r(j).*conj(r(j-i));    
    end
    tot
    Rk=tot/simlen;
    fnm=fnm+imag(Rk);
    fdm=fdm+i*real(Rk);
end
f_hat=fnm/(2*pi*Ts*fdm);
estimate(kk)=abs(f_hat-delf)/delf
end

plot(A,estimate);
grid on;
hold on;
% err = scipy.vectorize(estimate)
% plt.title("SNR vs Frequency Error with fixed frequency offset")
% plt.plot(A, err(A),label="QPSK Mapping,$\Delta f =5 MHz$")
% plt.xlabel('$SNR$')
% plt.ylabel('Error= $(\\frac{\Delta_f - \hat{f}}{\Delta_f})$')
% plt.legend(loc='best')
% plt.grid()
% plt.savefig("./frequencyestiamtion_best_error_vs_snr.eps")
% plt.show()