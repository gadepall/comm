#Code by GVV Sharma
#March 16, 2019
#released under GNU GPL
import numpy as np



a1 = 1
a2 = 1
b1 = 3
b2 = -1

A = np.array(([a1,a2],[b1,b2]))
x = np.linalg.det(A)
if x != 0:
  print('The lines intersect')
else:
  print('The lines do not intersect')
