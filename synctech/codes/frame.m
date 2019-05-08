snr=-2;
offset=0.1*pi*2;
phi0=0;
sof= [-1 1 1 -1 -1 -1 1 1 -1 1 -1 -1 1 -1 1 1 1 -1 1 -1 -1 -1 -1 -1 1 -1];
%length(sof)
Scramb= [0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,...
         0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0];
     
%length(Scramb)
b=[0 1 0 0 0 1 0];
pls=codage(b,Scramb);
plssof;

withoutplheader=[];

%=================================================================================
% Sending without PLHEADER, Only XFECFRAME. Calculation of False Alarm Probability.
for i=1:100
    i;
    x=sign(randn(1,360*(L_sof+L_pls)));
    y=canal(x,offset,phi0,snr);
    y=y./abs(y);
    d4=detec_sof_plus_pls_global(y,m_buf_filtre_sof,m_buf_filtre_pls);
    withoutplheader=[withoutplheader d4];
end;
%====================================================================================


%====================================================================================
% Sending XFECFRAME along with PLHEADER. Calculation of Missed Detection Probability.

x=kron(ones(1,10000),[sof pls sign(randn(1,64))]);
y=canal(x,offset,phi0,snr);
y=y./abs(y);
d4=detec_sof_plus_pls_global(y,m_buf_filtre_sof,m_buf_filtre_pls);
withplheader=d4(1:L_sof + L_pls +64:length(d4));
%=====================================================================================



%======================================================================================

%mini=min(min(withoutplheader),min(withplheader));
maxi=max(max(withplheader),max(withoutplheader));

for i=1:100
    threshold= (maxi)/99*(i-1);
    
    pfa3(i)=sum((sign(abs(withoutplheader)-threshold)+1)/2)/length(withoutplheader);
    pnd3(i)=sum((sign(threshold-abs(withplheader))+1)/2)/length(withplheader);
end;


%========================================================================================


%plot(sans_signald4)
semilogx(pfa3,pnd3);
xlabel('$P_{fa}$','Interpreter','latex')
ylabel('$P_{md}$','Interpreter','latex')
legend('Global Threshold ')
xlim([10^(-6) 10^(-2)]);
%title('Frame detection methods on DVB-S2  at -2 dB')
grid on;
