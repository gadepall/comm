function m_psk=mapping(dataSym)
M=8;
I=1/sqrt(2)*cos((dataSym-1)/M*2*pi);
Q=1/sqrt(2)*sin((dataSym-1)/M*2*pi);
m_psk=(I+1i*Q);
