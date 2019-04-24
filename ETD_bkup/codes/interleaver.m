function interdata=interleaver(dataSym)
kk=dataSym;
interdata1=reshape(kk,[],3);
interdata2=transpose(interdata1);
interdata=reshape(interdata2,[],1);
% interdata2=zeros(1,64800)
% for i=1:1:21600
%     for j=1:1:3
%         interdata2((i-1)*3+j)=interdata1(i:j)
%     end
% end
% interdata=interdata2

