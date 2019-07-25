#include <stdio.h>

float comm_diff(float,float,int);
int main(void)
{
FILE *fp;
float t_0 = -2.0, t_k = 8.0, d,t_n;
int k = 20, n;

//Common difference
d = comm_diff(t_0,t_k,k);
fp = fopen("ap.dat","w");
for(n = 0; n < k; n++)
{
t_n = t_0+n*d;
printf("%f\n",t_n);
fprintf(fp,"%f\n",t_n);
}
fclose(fp);
return 0;
}
float comm_diff(float first,float last,int n)
{
float d;
d = (last-first)/(n-1);
return d;
}
