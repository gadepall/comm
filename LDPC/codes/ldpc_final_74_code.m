clc;
clear;
H=[1 1 1 0 1 0 0;1 0 1 1 0 1 0 ; 1 1 0 1 0 0 1];
%H=[1 1 1 0 1 0 0;0 1 1 1 0 1 0 ; 1 1 0 1 0 0 1;1 0 1 0 1 1 1];


 Eb_N0_dB=0:1:9;
 Eb=7/4;
 ber=zeros(1,length(Eb_N0_dB));

MaxItrs=5;

% 
 frames=10000;
for snr=1:length(Eb_N0_dB)
for i=1:frames
%ip=randi([0 1],1,4);
ip=ones(1,4);
p=mod(H(:,[1:4])*transpose(ip),2);
c=[ip transpose(p)];
xc=2*c-1;

    N0= Eb/(exp(Eb_N0_dB(snr)*log(10)/10));
noise= sqrt(N0/2)*randn(1,length(xc));
rx=xc+noise;
%rx=[0.2 -0.3 1.2 -0.5 0.8 0.6 -1.1];
L=rx;
numOfEntries = sum(sum(H==1));
%msg matrix
rr=spalloc(3,7,numOfEntries);
itr=0;
NumC=0;
NumV=0;
sumcolumn=zeros(1,7);
Rcv = spalloc(3,7,numOfEntries); 
 for j=1:3              
          idx = find(H(j,:)==1); % slow
          S = L(idx)-full(Rcv(j,idx))  ;                
          for v=1:length(idx)    ;         
            Stmp = S;
            Stmp(v) = []; % clear row                 
            Rcv(j,idx(v)) = min(abs(Stmp))*prod(sign(Stmp));
                   
            % --variable node & check node computed
            NumC = NumC + 1; 
            NumV = NumV + 1;
          end
 end
 dum=[rx;full(Rcv)];
sumcolumn=sum(dum);
rr=Rcv;
for jj=1:7
    id = find(H(:,jj)==1); % slow 
    Rcv;
    for v=1:length(id)
        rr(id(v),jj)=sumcolumn(jj)-Rcv(id(v),jj);
        %L(idx(v)) = S(v) + Rcv(j,idx(v)); 
    end
end
L=rr;
while itr<MaxItrs-1
    sumcolumn=zeros(1,7);
    Rcv = spalloc(4,7,numOfEntries); 
 for j=1:3             
          idx = find(H(j,:)==1) ;% slow
          S = L(j,idx)-full(Rcv(j,idx))     ;             
          for v=1:length(idx)    ;         
            Stmp = S;
            Stmp(v) = []; % clear row                 
            Rcv(j,idx(v)) =min(abs(Stmp))*prod(sign(Stmp));        
            % --variable node & check node computed
            NumC = NumC + 1; 
            NumV = NumV + 1;
          end
 end
dum=[rx;full(Rcv)];
sumcolumn=sum(dum);
rr=Rcv;
for jj=1:7
    id = find(H(:,jj)==1); % slow 
    Rcv;
    for v=1:length(id)
        rr(id(v),jj)=sumcolumn(jj)-Rcv(id(v),jj);
        %L(idx(v)) = S(v) + Rcv(j,idx(v)); 
    end
end
L=Rcv;

    itr=itr+1;    
end
xhat=sumcolumn>0;
 error= sum(c(1,4)~=xhat(1,4))/(frames*4);
 ber(snr)=ber(snr)+error;
end

 end
 thber=0.5*erfc(sqrt(10.^(0.1*Eb_N0_dB)));
 semilogy(Eb_N0_dB,ber);
 hold on;
 semilogy(Eb_N0_dB,thber);
 grid on;
 legend('With Coding', 'Without Coding');
xlabel('$\frac{E_b}{N_0}$ dB','interpreter','latex');
ylabel('$P_e$','interpreter','latex');
%title('SNR vs BER curves for BPSK using LDPC Coding');