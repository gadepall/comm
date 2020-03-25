function d=detec_sof_plus_pls_global(y,m_buf_filtre_sof,m_buf_filtre_pls)
L_pls=64;
L_sof=26;
N=length(y);
y=[y zeros(1,L_sof+L_pls)];
for s3=[1,2,3,4,5,6]
    span(1,:)=y(1:N).*conj(y(1+(2^(s3-1)):N+(2^(s3-1))));
    dn1(1,:)=conv(span(1,:),m_buf_filtre_pls((2^(s3-1)),:));
    dn2(1,:)=conv(span(1,:),m_buf_filtre_sof((2^(s3-1)),:));
    clear span;
    d_pls(s3,:)=[dn1(1,L_pls+L_sof-(2^(s3-1)):length(dn1)) zeros(1,L_pls+L_sof-1-(2^(s3-1)))];
    d_sof(s3,:)=[dn2(1,L_pls+L_sof:length(dn2)) zeros(1,L_pls+L_sof-1)];
    clear dn1;
    clear dn2;
end;
d=sum(max(abs(d_sof+d_pls),abs(d_sof-d_pls)));
