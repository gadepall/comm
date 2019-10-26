clc;
close all;
clear all;
TimeSlot=2e-3; %Transmit time duration
SNR = 18; %Signal to noise ratio
Rs = 185e3; % symbol rate
a=[1+0i 1/sqrt(2)+1i*1/sqrt(2) 1i -1/sqrt(2)+1i*1/sqrt(2) -1 -1/sqrt(2)-1i*1/sqrt(2) -1i 1/sqrt(2)-1i*1/sqrt(2) ];
Ak = a(randi(8,20000,1)); % 8 PSK sequence of 1000 samples
figure(1); plot(real(a),imag(a),'*'); title('8PSK constellation'); grid;

%% Channel creation and channel modelling
Rsym = Rs; M = 8;                  % Input symbol rate
Rbit = Rsym * log2(M);      % Input bit rate
Nos = 1;                    % Oversampling factor
ts = (1/Rsym) / Nos;        % Input sample period
v = 60 * 1e3/3600;         % Mobile speed (m/s)
fc = 180e6;                % Carrier frequency
c = 3e8;                    % Speed of light in free space
% fd = v*fc/c;                % Maximum Doppler shift of diffuse component
fd=.1;
kFactor = 0.87/0.13;    % Note: we use the value from 3GPP TS 45.005 V7.9.0
fdLOS = 0.7 * fd;
RAx4PathDelays = [0.0 0.2 0.4 0.6 0.8] * 1e-5; %These values are not accurate only for trail.
RAx4AvgPathGaindB = [0 -2 -10 -20 -22];%These values are not accurate only for trail.
chan = ricianchan(ts, fd, kFactor, RAx4PathDelays, RAx4AvgPathGaindB, fdLOS)
10*log10((abs(chan.PathGains)).^2)
% This setting is needed to store quantities used by the channel
% visualization tool.
chan.StoreHistory = 1;
% After each frame is processed, the channel is not reset: this is
% necessary to preserve continuity across frames.
chan.ResetBeforeFiltering = 0;
% This setting makes the total average power of all path gains be
% equal to 1.
chan.NormalizePathGains = 1; Nframes = 1;
Nsamples=TimeSlot*(Rsym)*Nos;
%%
%%Channel Addition
chan.PathGains
Rk = filter(chan, Ak);
plot(chan);
noise = (1/sqrt(2))*(randn(size(Rk)) + 1j*randn(size(Rk))); %Initial noise vector
P_s = var(Rk); % Signal power
P_n = var(noise); % Noise power
% Defining noise scaling factor based on the desired SNR:
noise_scaling_factor = sqrt(P_s/P_n./10.^(SNR./10)); 
Rk_noisy=Rk+noise*noise_scaling_factor; % Received signal
figure(2);  plot(real(Rk),imag(Rk),'*');legend('Received constellation')
%%
%%%%%%%%%%%%%%%%%%%%%%%LMS Algorithm%%%%%%%%%%%%%%%%
hTap=11;%Channel Taps
beta = 0.001; % step-size of the algorithm
c_LMS = zeros(hTap,1); % equalizer coefficients, initializations
for i = (hTap+1)/2:length(Rk_noisy)-(hTap-1)/2 
rk = flipud(Rk_noisy(i-(hTap-1)/2 :i+(hTap-1)/2).'); % Received signal vector
Ek(i) = Ak(i) - c_LMS.'*rk; % Error signal, we assume a known symbol sequence
c_LMS = c_LMS + beta*Ek(i)*conj(rk); % LMS update !
end
%% MSE Equalizer 
% Initialization
FII = zeros(hTap,hTap); % Autocorrelation Matrix initialization
alfa = zeros(hTap,1); % Cross-correlation vector initialization
% Estimating FII and alfa using sample estimates based on training symbols
% Notice that here we use all the generated data as training symbols
for i = (hTap+1)/2:length(Rk_noisy)-(hTap-1)/2 %16:length(Rk_noisy)-15, 
% rk = flipud(Rk_noisy(i-15:i+15).'); % Received signal vector
rk = flipud(Rk_noisy(i-(hTap-1)/2 :i+(hTap-1)/2).'); % Received signal vector
FII = FII + rk*conj(rk).'; % Autocorrelation matrix
alfa = alfa + Ak(i)*conj(rk); 
end
% FII
FII = FII/(length(Rk_noisy)-(hTap-1)); % Final sample estimate of the autocorrelation matrix
alfa = alfa/(length(Rk_noisy)-(hTap-1)); % Final sample estimate of the cross-correlation vector
c_MSE = inv(conj(FII))*alfa; % Equalizer coefficients
%%
% Plotting
figure(3);
subplot(121);
y_LMS=filter(c_LMS,1,Rk);
plot(y_LMS,'rx'); 
title('LMS Equalized Constellation');
grid on;
subplot(122);
y_MSE=filter(c_MSE,1,Rk);
plot(y_MSE((hTap+1)/2:end),'rx');
title('MSE Equalized Constellation');
grid on;