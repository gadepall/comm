clc;
clear all;
close all;

%% Initialization of Variables
%M1 = input("Number of symbols in the first cirle M1 = ");
%M2 = input("Number of symbols in the second circle M2 = ");
%M3 = input("Number of symbols in the third circle M3 = ");
M1=4;
M2=12;
R1 = sqrt(7);
R2 = 3*sqrt(7);
n=64800;
%n = input("Number of transmission bits n = ");
% Generate vector of binary data
DataIn = randi([0 1],n,1); 
%DataIn=[0;0;0;1;0;0;0;1;1;0;1;1;1;1;1;0;1;1;0;0;0;1;0;1;1;1;0;0;0;1];
% Constallation bits
CBC1 = load('cb16_1.csv');
CBC2 = load('cb16_2.csv');
CB = [CBC1; CBC2];
% Constallation Symbols
load('csc1.mat');
load('csc2.mat');

CS = [CSC1; CSC2];


%% Modulation  
k = log2(M1 + M2 );
%con_symbol = reshape(DataIn, length(DataIn)/k, k);
con_symbol0=reshape(DataIn,k,[]);
con_symbol=transpose(con_symbol0);
Tx_signal = [];
for i = 1:length(con_symbol)
    for j = 1:length(CB)
    if isequal(con_symbol(i,:),CB(j,:))
        Tx_signal(i,:) = CS(j,:);
    end 
    end
end

% Signal 2 Noise Ratio in dB
SNRdB = 0:1:30; 
for snr = 1:length(SNRdB)
%% AWGN Channe
Rx_signal = awgn(Tx_signal,SNRdB(snr),'measured');
%Rx_signal = Tx_signal;
%% Demodulation
for i=1:length(Rx_signal)
    R(i)=abs(Rx_signal(i));
    An(i)=angle(Rx_signal(i));
%     if An(i)<0
%         An(i)=2*pi-An(i)
%     end
end
for i=1:length(Rx_signal)
    if An(i)<0
         An(i)=2*pi+An(i);
    end
end
% R = abs(Rx_signal);
% An = angle(Rx_signal);

for i = 1:length(Rx_signal)
    if R(i) <=(R1+R2)/2
        if (An(i)>0) && (An(i)<=(pi/2))
            Rx_symbol(i,:) = CBC1(1,:);
        elseif (An(i)>pi/2) && (An(i)<=(pi))
            Rx_symbol(i,:) = CBC1(2,:);
        elseif (An(i)>pi) && (An(i)<=(3*pi/2))
            Rx_symbol(i,:) = CBC1(3,:);
        else
            Rx_symbol(i,:) = CBC1(4,:);
        end
   
    else
        if (An(i)>=0) && (An(i)< pi/6)
            Rx_symbol(i,:) = CBC2(1,:);
        elseif (An(i)>=pi/6) && (An(i)< 2*pi/6)
            Rx_symbol(i,:) = CBC2(2,:);
        elseif (An(i)>=2*pi/6) && (An(i)< 3*pi/6)
            Rx_symbol(i,:) = CBC2(3,:);
        elseif (An(i)>=3*pi/6) && (An(i)< 4*pi/6)
            Rx_symbol(i,:) = CBC2(4,:);
        elseif (An(i)>=4*pi/6) && (An(i)< 5*pi/6)
            Rx_symbol(i,:) = CBC2(5,:);
        elseif (An(i)>=5*pi/6) && (An(i)< 6*pi/6)
            Rx_symbol(i,:) = CBC2(6,:);
        elseif (An(i)>=6*pi/6) && (An(i)< 7*pi/6)
            Rx_symbol(i,:) = CBC2(7,:);
        elseif (An(i)>=7*pi/6) && (An(i)< 8*pi/6)
            Rx_symbol(i,:) = CBC2(8,:);
        elseif (An(i)>=8*pi/6) && (An(i)< 9*pi/6)
            Rx_symbol(i,:) = CBC2(9,:);
        elseif (An(i)>=9*pi/6) && (An(i)< 10*pi/6)
            Rx_symbol(i,:) = CBC2(10,:);
        elseif (An(i)>=10*pi/6) && (An(i)< 11*pi/6)
            Rx_symbol(i,:) = CBC2(11,:);
        else
            Rx_symbol(i,:) = CBC2(12,:);
        end                       
    end   
end
%DataOut = Rx_symbol(:);
DataOut1=transpose(Rx_symbol);
DataOut=reshape(DataOut1,[],1);

% BER Performence
[numErrors(snr),ber(snr)] = biterr(DataIn, DataOut);
 end 

semilogy(SNRdB, ber);
grid on;
%title(' SNR vs BER for 16APSK');
xlabel('$\frac{E_b}{N_0}$dB','interpreter','latex');
ylabel('$P_e$','interpreter','latex');