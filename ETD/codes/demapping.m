function y=demapping(rx)
M=8;
received=rx;
s_i=zeros(1,M);
s_q=zeros(1,M);
for i=1:1:M
    s_i(i)=1/sqrt(2)*cos((i-1)/M*2*pi);
    s_q(i)=1/sqrt(2)*sin((i-1)/M*2*pi);
end
r_i=real(received);
r_q=imag(received);
r_i_repmat=repmat(r_i,1,M);
r_q_repmat=repmat(r_q,1,M);
distance=zeros(length(r_i),M);
minDistIndex=zeros(length(r_i),1);
for j=1:1:length(r_i)
    distance(j,:)=(r_i_repmat(j,:)-s_i).^2+(r_q_repmat(j,:)-s_q).^2;
    [dummy,minDistIndex(j)]=min(distance(j,:));
end
y=minDistIndex;