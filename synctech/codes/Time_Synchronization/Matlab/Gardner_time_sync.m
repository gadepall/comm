clc;
clear all;
close all;
%=========================================================================================
% This program implemented based on the ""A BPSK/QPSK Timing-Error Detector for Sampled
% Receivers by FLOYD M.GARDNER,IEEE TRANSACTIONS ON COMMUNICATIONS, VOL.COM-34,NO. 5,
% MAY 1986"". This is a simple algorithm for detection of timing error of a synchronous,
% bandlimited, BPSK or QPSK datastrem. The algorithm requires two samples for symbol. And
% uses one of the two samples for the Symbol decision. It's purely a non data aided Timing
% Error detection.
%=========================================================================================



%=========================================================================================
% Inputs : 1) Simulation Length (N) (Total number of symbols)
%	   2) Samples per Symbol (M)
%          3) Eb_N0_dB Range
%          4) Length_Prev_Symbols (For averange purpose)
%
% Output : 1) BER_sim

% Plot : BER Curve for theorical simulation vs Algorithm             
%==========================================================================================

%==========================================================================================
%                                      Transmitter
%==========================================================================================

N=100000 ;   % Simulation length
data=rand(1,N)>0.5; % Generation of random bits
c=2*data-1;  % BPSK mapping
M=100;     % Number of samples per symbol.
p=ones(1,M);            % shape Pulse shape
Mapped_Data=zeros(1,N*M); % Total samples
Mapped_Data(1:M:end)=c ; %Interpolated BPSK data using the pulse shaping filter(NRZ)
Mapped_Data=conv(Mapped_Data,p);

%%%%==========================================================================================
%%%% Noise addition
Eb_N0_dB=1:1:10; % Signal to Noise Ratio
len_eb_n0=length(Eb_N0_dB);        
time_offsets=([3,50,80]);  % List of Timing Offsets
len_time_offsets=length(time_offsets);
BER_sim=zeros(len_time_offsets,len_eb_n0) ;  % Bit Error Rate Values
 for off=1:len_time_offsets
     for i=1:len_eb_n0
         %========================================================
         % Noise characteristics
         N0 = 10^(Eb_N0_dB(i)/10);
         noise=sqrt(1/(2*N0))*randn(1,length(Mapped_Data));
         %=========================================================
         rx=Mapped_Data+noise;   % Noisy received samples
         delta=M/2;
         timing_offset=time_offsets(off);  % Timing offset addition 
         center=delta + timing_offset;  % New center
         %===========================================================
         %                 Gardner TED algorithm
         %===========================================================
         Decision_Samples=zeros(1,N); %Samples storing for making Decision. (DS)
         Length_Prev_Symbols=6;     %User Specified Le: Used for the Averaging Purpose
         Prev_Samples=zeros(1,Length_Prev_Symbols);
         increment=1;
         index_DS=0;   % Index of Decision samples while storing the data.
         tau=0;
         for k=delta:M:length(rx)-delta
             index_DS=index_DS+1;
             m_s=rx(center);   % Middle sample
             l_s=rx(center+delta); % Late sample
             e_s=rx(center-delta); % Early sample
             Decision_Samples(index_DS)=e_s ; %As per the algorithm.
             sub=l_s-e_s;
             Prev_Samples(mod(index_DS,Length_Prev_Symbols)+1)=sub*m_s ; % Algorithm specified
             if mean(Prev_Samples)>0
                 tau=-increment;
             else
                 tau=increment;
             end
             center=center+M+tau;
             if center>=length(rx)- delta-1
                 break;
             end               
         end
         
             %===============================================================
             
                   % Decision and Bit Error Rate Calulation
     Error=0; %Set the initial value for Error         
    for k=1:N-1 %Error calculation
        if ((Decision_Samples(k)>0 && c(k)==-1)||(Decision_Samples(k)< 0 && c(k)==1))
            Error=Error+1;
        end
    end
    BER_sim(off,i)=Error/(N-1);
    end
 end
BER_th=(1/2)*erfc(sqrt(10.^(Eb_N0_dB/10))); %Calculate The theoretical BER
figure
semilogy(Eb_N0_dB,BER_th); %Plot theoretical BER
hold on
semilogy(Eb_N0_dB,BER_sim(1,:)); %Plot simulated BER
hold on
semilogy(Eb_N0_dB,BER_sim(2,:)); %Plot simulated BER
hold on
semilogy(Eb_N0_dB,BER_sim(3,:)); %Plot simulated BER
title('SNR Vs. BER for BPSK­Gardner technique');
legend('Theoritical','\tau=3','\tau=50','\tau=80','Interpreter','latex');
xlabel('$\frac{E_b}{N_0}$(dB)','Interpreter','latex')
ylabel('$P_e$','Interpreter','latex')