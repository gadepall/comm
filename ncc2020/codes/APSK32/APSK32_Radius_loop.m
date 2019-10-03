%% APSK MAPPING Schemes for DVB-S2
% Author : K. Prasanna kumar

clc;
clear all;
close all;

%% Initialization of Variables
% M1 = input("Number of symbols in the first cirle M1 = ");
% M2 = input("Number of symbols in the second circle M2 = ");
% M3 = input("Number of symbols in the third circle M3 = ");
M1=4;
M2=12;
M3=16;
R1 = sqrt(7);
R2 = 3*sqrt(7);
R3 = 9*sqrt(7);
n=64800;
%n = input("Number of transmission bits n = ");
% Generate vector of binary data
DataIn = randi([0 1],n,1); 
% Constallation bits
CBC1 = load("CBC1.csv");
CBC2 = load("CBC2.csv");
CBC3 = load("CBC3.csv");
CB = [CBC1; CBC2;CBC3];
% Constallation Symbols
load('csc1.mat');
load('csc2.mat');
load('csc3.mat');
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

% Signal 2 Noise Ratio in dB
SNRdB = 0:1:20; 
for snr = 1:length(SNRdB)
%% AWGN Channe
Rx_signal = awgn( Tx_signal,SNRdB(snr),'measured');
%% Demodulation
R = abs(Rx_signal);

for i = 1:length(Rx_signal)
    if R(i) <=(R1+R2)/2
        for j = 1: length(CSC1)
            sd1(j) = abs(Rx_signal(i,:) - CSC1(j,:));
        end
        [~, x1] =  min(sd1);
        Rx_symbol(i,:) = CBC1(x1,:);
    elseif (R(i) > (R1+R2)/2) && (R(i) < (R3+R2)/2)
            for j = 1:length(CSC2)
                sd2(j) = abs(Rx_signal(i,:)- CSC2(j,:));
            end
            [~, x2] =  min(sd2);
            Rx_symbol(i,:) = CBC2(x2,:);
    else  
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
    
