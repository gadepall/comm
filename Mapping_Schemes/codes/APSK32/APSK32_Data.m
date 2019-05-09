%% Data for 32APSK
%function [CB, CS] = data32apsk(M1,M2,M3)

CBC1 = load('CBC1.csv');
CBC2 = load('CBC2.csv');
CBC3 = load('CBC3.csv');
%CB = [CBC1; CBC2 ; CBC3];



M1 = 4; R1 = sqrt(7);
M2 = 12; R2 = 3*sqrt(7);
M3 = 16; R3 = 3*R2;
CSC1 = [];
for n1 = 1: M1
    CSC1(n1,:) = R1*exp(j*(((n1-1)*2*pi)/M1 + pi/4));
end
save("csc1",'CSC1')
CSC2 = [];
for n2 = 1: M2
    CSC2(n2,:) = R2*exp(j*(((n2-1)*2*pi)/M2 + pi/4));
end
save('csc2',"CSC2")
CSC3 = [];
for n3 = 1: M3
    CSC3(n3,:) = R3*exp(j*(((n3-1)*2*pi)/M3));
end
save('csc3',"CSC3")

%CS =[CSC1; CSC2; CSC3];

%end