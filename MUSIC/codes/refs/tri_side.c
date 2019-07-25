#include <stdio.h>
#include <math.h>
//verify if given lengths 
//are sides of a triangle.
int main(void)
{
float a,b,c;

printf("Enter the sides of the triangle\n");
scanf("%f %f %f", &a,&b,&c);

if(a+b <  c)
{
printf("No triangle\n");
}
else if(b+c <  a)
{
printf("No triangle\n");
}
else if(c+a <  b)
{
printf("No triangle\n");
}
else
{
printf("Yes Triangle\n");
}
return 0;
}
