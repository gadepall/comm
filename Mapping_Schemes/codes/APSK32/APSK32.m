%% APSK MAPPING Schemes for DVB-S2
% Author : K. Prasanna kumar

clc;
clear all;
close all;

%% Initialization of Variables
M1 = input("Number of symbols in the first cirle M1 = ");
M2 = input("Number of symbols in the second circle M2 = ");
M3 = input("Number of symbols in the third circle M3 = ");
R1 = sqrt(7);
R2 = 3*sqrt(7);
R3 = 9*sqrt(7);
n = input("Number of transmission bits n = ");
% Generate vector of binary data
DataIn = randi([0 1],n,1); 
% Constallation bits
CBC1 = [1,0,0,0,1;1,0,0,1,1;1,0,1,0,1;1,0,1,1,1];
CBC2 =[1,0,0,0,0; 1,0,0,1,0; 1,0,1,0,0; 1,0,1,1,0; 0,0,0,0,0; 0,0,0,1,0; 0,0,1,0,0; 0,0,1,1,0; 0,0,0,0,1; 0,0,0,1,1; 0,0,1,0,1;0,0,1,1,1];
CBC3 =[1,1,0,0,0; 0,1,1,0,1; 1,1,1,1,0; 0,1,0,1,1; 0,1,0,0,0; 1,1,0,1,0; 1,1,1,0,0; 0,1,1,1,0;1,1,0,0,1; 0,1,0,1,0;0,1,1,0,0;1,1,1,1,1;0,1,0,0,1;1,1,0,1,1;1,1,1,0,1;0,1,1,1,1];
CB = [CBC1; CBC2;CBC3];
% Constallation Symbols
CSC1 = [R1*exp(j*pi/4);R1*exp(j*-pi/4);R1*exp(j*3*pi/4); R1*exp(j*-3*pi/4)];
CSC2 = [R2*exp(j*pi/12);R2*exp(j*-pi/12);R2*exp(j*(pi-pi/12));R2*exp(j*(pi+pi/12));R2*exp(j*pi/4);R2*exp(j*-pi/4);R2*exp(j*3*pi/4); R2*exp(j*-3*pi/4);R2*exp(j*5*pi/12);R2*exp(j*-5*pi/12);R2*exp(j*(pi-5*pi/12));R2*exp(j*(pi+5*pi/12))];
CSC3 = [R3*exp(j*0); R3*exp(j*pi/2); R3*exp(j*pi); R3*exp(j*-pi/2);R2*exp(j*pi/8);R2*exp(j*-pi/8);R2*exp(j*(pi-pi/8));R2*exp(j*(pi+pi/8)); R3*exp(j*pi/4);R3*exp(j*-pi/4);R3*exp(j*3*pi/4); R3*exp(j*-3*pi/4);  R3*exp(j*3*pi/8);R3*exp(j*-3*pi/8);R3*exp(j*(pi-3*pi/8));R3*exp(j*(pi+3*pi/8))];
CS = [CSC1; CSC2; CSC3];
%% Modulation  
k = log2(M1 + M2 + M3);
con_symbol = reshape(DataIn, length(DataIn)/k, k);
Tx_signal = [];
for i = 1:length(con_symbol)
    for j = 1:length(CB)
    if isequal(con_symbol(i,:),CB(j,:))
        Tx_signal(i,:) = CS(j,:);
    end 
    end
end

%% Signal 2 Noise Ratio in dB
SNRdB = 0:1:20; 
for snr = 1:length(SNRdB)
%% AWGN Channe
Rx_signal = awgn( Tx_signal,SNRdB(snr),'measured');
%% Demodulation
R = abs(Rx_signal);
for i = 1:length(Rx_signal)
    d = [abs(R(i)- R1); abs(R(i)- R2); abs(R(i)- R3) ];
    [~, y] =  min(d);
    switch y
        case 1
            for j = 1: length(CSC1)
                sd1(j) = abs(Rx_signal(i,:) - CSC1(j,:));
            end 
            [~, x1] =  min(sd1);
            Rx_symbol(i,:) = CBC1(x1,:);
        case 2
            for j = 1: length(CSC2)
                sd2(j) = abs(Rx_signal(i,:) - CSC2(j,:));
            end
            [~, x2] =  min(sd2);
            Rx_symbol(i,:) = CBC2(x2,:);
        case 3
            for j = 1: length(CSC3)
                sd3(j) = abs(Rx_signal(i,:) - CSC3(j,:));
            end
            [~, x3] =  min(sd3);
            Rx_symbol(i,:) = CBC3(x3,:);
    end
end
DataOut = Rx_symbol(:);

%% BER Performence
[numErrors(snr),ber(snr)] = biterr(DataIn, DataOut);
end 

semilogy(SNRdB, ber);
grid on;
title(' BER performance against SNR without channel coding');
xlabel('SNR in dB');
ylabel('BER Performance')
    
