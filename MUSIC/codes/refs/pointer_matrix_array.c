#include <stdio.h>
#include <stdlib.h>

//This program shows how to use pointers as 2-D arrays

//Function declaration
double **createMat(int m,int n);
void readMat(int m,int n,double **p);
void print(int m,int n,double **p);
//End function declaration

int  main() //main function begins
{

//Defining the variables
int m,n;//integers
double **a;

printf("Enter the size of the matrix m  n \n");
scanf("%d %d", &m,&n);


printf("Enter the values of the matrix\n");
a = createMat(m,n);//creating the matrix a
readMat(m,n,a);//reading values into the matrix a
print(m,n,a);//printing the matrix a

return 0;
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
