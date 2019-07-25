#include <stdio.h>
//sum to n terms of an AP
//t_0 = first term
//t_n = nth  term
//d = commo difference
//k = number of terms

int main(void)
{
float t_0 = 1, d = 1,s_n, t_n;
int k = 10, n;

s_n = 0;
//For Loop 
for(n = 0; n < k; n++)
{
t_n = t_0 + n*d;
s_n = s_n+t_n;
}
printf("%f\n",s_n);
return 0;
}
