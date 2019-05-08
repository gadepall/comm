L_sof=26;
L_pls=64;
inverse_index_sof=L_sof:-1:1;
sofI=[sof(inverse_index_sof) zeros(1,L_sof)];
for s=1:L_sof-1
    sof_r(1,:)=sofI(1:L_sof).*sofI(1+s:L_sof+s);
    sof_m_r(s,:)=circshift(sof_r(1,:),[0 s]);
    clear sof_r;
end;
sof_m_b_r=[sof_m_r;zeros(7,26)];
m_buf_filtre_sof=[zeros(32,64) sof_m_b_r];

inverse_index_pls=L_pls:-1:1;
plsI=[pls(inverse_index_pls) zeros(1,L_pls)];
for s=1:6
    filtre(s,:)=kron(ones(1,2^(6-s)),[ones(1,2^(s-1)) zeros(1,2^(s-1))]);
end
filtre_r=[filtre(1,:);filtre(2,:);zeros(1,64);filtre(3,:);zeros(3,64);...
    filtre(4,:);zeros(7,64);filtre(5,:);zeros(15,64);filtre(6,:)];
for s1=[1,2,4,8,16,32]
    pls_r(s1,:)=plsI(1:L_pls).*plsI(1+s1:L_pls+s1);
end
for s2=[1,2,4,8,16,32]
    filtre_pls(s2,:)=pls_r(s2,:).*filtre_r(s2,:);
end
m_buf_filtre_pls=[filtre_pls zeros(32,26)];