#Code by GVV Sharma
#March 14, 2019
#released under GNU GPL
import numpy as np

def det(A):
  a1 = A[0][0]
  a2 = A[0][1]
  b1 = A[1][0]
  b2 = A[1][1]
  y = a1*b2 - a2*b1
  return y


a1 = 1
a2 = 1
b1 = 3
b2 = -1

A = np.array(([a1,a2],[b1,b2]))
x = det(A)
print(x)
