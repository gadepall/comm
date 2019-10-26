function Y=codage(b,Scramb)
G=def_G();
Y=mod(b(1:6)*G,2);
Y=kron(Y,[1 1]);
b7=kron(ones(1,32),[0  b(7)]);
Y=mod(Y+b7,2);
%Scrambling 
Y=xor(Y,Scramb);

Y=2*Y-1;