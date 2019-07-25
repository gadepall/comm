#include <stdio.h>
#include <math.h>
//nth term of a GP
//t_0 = first term
//t_n = nth  term
//r = common ratio
//k = number of terms

int main(void)
{
float t_0 = 1, r = 2, t_n;
int  n = 3;

t_n = t_0*pow(r,n);
printf("%f\n",t_n);
return 0;
}
