M=8;
N=64800;
EbN0dB=0:2:12;
Rc=1;
k=3;
EsN0dB=EbN0dB+10*log10(3);
dataSym=ceil(M.*rand(N,1));
da=interleaver(dataSym);
m_psk=mapping(da);
simulatedSER=zeros(1,length(EsN0dB));
index=1;
for x=EsN0dB
    %disp(x)
    EsN01in=10.^(x/10);
   %disp(EsN01in)
    noiseSigma=1/sqrt(2)*sqrt(1/(2*Rc*EsN01in));
    %EbN0=EsN0/(Rm*Rc);
    noise=noiseSigma*(randn(length(m_psk),1)+1i*randn(length(m_psk),1));
    received=m_psk+noise;
    y=demapping(received);
    y=deinterleaver(y);
    y=transpose(y);
    simulatedSER(index)=sum(y~=dataSym)/N;
    index=index+1;
    % disp(simulatedSER)
end
EbN01in=10.^(EbN0dB/10);
theoreticalSER=(erfc(sqrt(EbN01in*k)*sin(pi/M)));

semilogy(EbN0dB,(simulatedSER),'r')
hold on
semilogy(EbN0dB,theoreticalSER,'b-*')
legend('With Interleaver', 'Without Interleaver');
xlabel('$\frac{E_b}{N_0}$(dB)','Interpreter','latex')
ylabel('$P_e$','Interpreter','latex')
saveas(gcf,'Interleaver','eps')


