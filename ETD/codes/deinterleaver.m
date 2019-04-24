function y = deinterleaver(r)
id1=reshape(r,3,[]);
id2=transpose(id1);
id3=reshape(id2,[],1);
%id4=reshape(id2,1,[]);
y=transpose(id3);

% interdata2=zeros(64800)
% for j=1:1:3
%     for i=1:1:21600
%         interdata2((i-1)*3+j)=interdata1(j:i)
%     end
% end