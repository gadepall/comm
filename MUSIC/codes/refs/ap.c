#include <stdio.h>

int main(void)
{
FILE *fp;
float t_0 = -2.0, t_k = 8.0, d,t_n;
int k = 20, n;

//Common difference
d = (t_k-t_0)/(k-1);
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
