clc;
clear all;
close all;
M=8;
N=64800;
EbN0dB=0:1:18;
k=log2(M);
EsN0dB=EbN0dB+10*log10(k);
dataSym=ceil(M.*rand(N,1));
%da=interleaver(k,dataSym);
m_psk=mapping(M,dataSym);
simulatedSER=zeros(1,length(EsN0dB));
index=1;
for x=EsN0dB
    %disp(x)
    EsN01in=10.^(x/10);
   %disp(EsN01in)
    noiseSigma=1/sqrt(2)*sqrt(1/(2*EsN01in));
    %EbN0=EsN0/(Rm*Rc);
    noise=noiseSigma*(randn(length(m_psk),1)+1i*randn(length(m_psk),1));
    received=m_psk+noise;
    y=demapping(M,received);
   % y=deinterleaver(k,y);
    %y=transpose(y);
    simulatedSER(index)=sum(y~=dataSym)/N;
    index=index+1;
    % disp(simulatedSER)
end
EbN01in=10.^(EbN0dB/10);
theoreticalSER=(erfc(sqrt(EbN01in*k)*sin(pi/M)));

plot(EbN0dB,(simulatedSER),'r');
hold on;
plot(EbN0dB,theoreticalSER,'b-*');
grid on;
legend('SimSER', 'TheorySER');
xlabel('$\frac{E_b}{N_0}$(dB)','Interpreter','latex')
ylabel('$P_e$','Interpreter','latex')
saveas(gcf,'Interleaver','eps')


