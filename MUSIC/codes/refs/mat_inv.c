#include <stdio.h>
#include <stdlib.h>

//This program shows how to use pointers as 2-D arrays

//Function declaration
double **createMat(int m,int n);
void readMat(int m,int n,double **p);
void print(int m,int n,double **p);
double detMat(double **p);
double **invMat(double **p);


//End function declaration

int  main() //main function begins
{

//Defining the variables
int m,n;//integers
double **A,**A_inv,det;

m = 2;
n = 2;
printf("Enter the values of the matrix\n");
A = createMat(m,n);//creating the matrix 
det = detMat(A);
readMat(m,n,A);//reading values into the matrix a
A_inv = invMat(A);
print(m,n,A_inv);//printing the matrix a

return 0;
}

double **invMat(double **p)
{
double **q, det;
det = detMat(p);
q = createMat(2,2);
q[0][0] = p[1][1]/det;
q[0][1] = -p[0][1]/det;
q[1][0] = -p[1][0]/det;
q[1][1] = p[0][0]/det;
return q;
}

double detMat(double **A)
{
double det;
det = A[0][0]*A[1][1]-A[0][1]*A[1][0];
return det;
}

//Defining the function for matrix creation
double **createMat(int m,int n)
{
 int i;
 double **a;
 
 //Allocate memory to the pointer
a = (double **)malloc(m * sizeof( *a));
    for (i=0; i<m; i++)
         a[i] = (double *)malloc(n * sizeof( *a[i]));

 return a;
}
//End function for matrix creation


//Defining the function for reading matrix 
void readMat(int m,int n,double **p)
{
 int i,j;
 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  {
   scanf("%lf",&p[i][j]);
  }
 }
}
//End function for reading matrix



//Defining the function for printing
void print(int m,int n,double **p)
{
 int i,j;

 for(i=0;i<m;i++)
 {
  for(j=0;j<n;j++)
  printf("%lf ",p[i][j]);
 printf("\n");
 }
}
