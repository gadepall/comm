%%Channel Model

clc;
clear all;
close all;

M = 8;                      % Modulation order

hMod = comm.PSKModulator(M, 'PhaseOffset', 0); % PSK Modulator System object

Rsym = 185e3;                % Input symbol rate
Rbit = Rsym * log2(M);      % Input bit rate
Nos = 4;                    % Oversampling factor
ts = (1/Rsym) / Nos;        % Input sample period

v = 60 * 1e3/3600;         % Mobile speed (m/s)
fc = 180e6;                % Carrier frequency
c = 3e8;                    % Speed of light in free space
% fd = v*fc/c;                % Maximum Doppler shift of diffuse component
fd=100;
kFactor = 0.87/0.13;    % Note: we use the value from 3GPP TS 45.005 V7.9.0
fdLOS = 0.7 * fd;
RAx4PathDelays = [0.0 0.2 0.4 0.6 0.8] * 1e-5; %Yet to finalise these values
RAx4AvgPathGaindB = [0 -2 -10 -20 -24]; %Yet to finalise these values

chan = ricianchan(ts, fd, kFactor, RAx4PathDelays, RAx4AvgPathGaindB, fdLOS)  %Assuming Rician Channel
10*log10((abs(chan.PathGains)).^2)
% This setting is needed to store quantities used by the channel
% visualization tool.
chan.StoreHistory = 1;
% After each frame is processed, the channel is not reset: this is
% necessary to preserve continuity across frames.
chan.ResetBeforeFiltering = 0;
% This setting makes the total average power of all path gains be
% equal to 1.
chan.NormalizePathGains = 1;

Nframes = 1;
% Nsamples = 1e4;

TimeSlot=2e-3;
Nsamples=TimeSlot*(Rsym)*Nos;
for iFrames = 1:Nframes
    y = filter(chan, step(hMod, randi([0 M-1],Nsamples,1)));
    plot(chan);
    % Select the Doppler spectrum as the current visualization.
    if iFrames == 1, channel_vis(chan, 'visualization', 'doppler'); end;
end

% channel_vis(chan, 'visualization', 'scattering');

% Nframes = 6;
% for iFrames = 1:Nframes
%     y = filter(chan, step(hMod, randi([0 M-1],Nsamples,1)));
%     plot(chan);
% end
x=abs(chan.PathGains(:,1));
t=ts:ts:(Nsamples)*ts;
fs=1/ts;
f=[0:(length(x)-1)]*fs/(length(x));
fprintf(' Total Transmit Duration=%f sec,Transmit Duration of One Frame=%f, Coherence Time=%f sec\n',(chan.NumSamplesProcessed)/(Rsym*Nos),Nsamples/(Rsym*Nos),1/fd);
fprintf('Rms Delay Spread=%e ,Coherence Bandwidth =%f\n',rms(RAx4PathDelays),1/(rms(RAx4PathDelays)));
figure(2);
subplot(421);
plot(t,abs(chan.PathGains(:,1)));
subplot(422);
plot(f,10*log10(abs(fft(chan.PathGains(:,1)))));
subplot(423);
plot(t,abs(chan.PathGains(:,2)));
subplot(424);
plot(f,10*log10(abs(fft(chan.PathGains(:,2)))));

subplot(425);
plot(t,abs(chan.PathGains(:,3)));

subplot(426);
plot(f,10*log10(abs(fft(chan.PathGains(:,3)))));
subplot(427);
plot(t,abs(chan.PathGains(:,4)));

subplot(428);
plot(f,10*log10(abs(fft(chan.PathGains(:,4)))));
figure(3);
x=10*log10(abs(fft([chan.PathGains(end,1) chan.PathGains(end,2) chan.PathGains(end,3) chan.PathGains(end,4) zeros(1,length(f)-4)])));
plot(f,fftshift(x));
title('Frequency Response as seen by the last sample');
% ylim([-40 10]);
grid on;

figure(4);
plot(t,10*log10(abs(chan.PathGains(:,1))),t,10*log10(abs(chan.PathGains(:,2))),t,10*log10(abs(chan.PathGains(:,3))),t,10*log10(abs(chan.PathGains(:,4))));
grid on;
title('multipath components in dB');