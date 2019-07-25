#include <stdio.h>
#include <math.h>

float circumference(float);
int main(void)
{
printf("%f\n",circumference(0.5));
return 0;
}
float circumference(float r)
{
return 2*M_PI*r;
}
