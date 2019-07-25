#Code by GVV Sharma
#March 26, 2019
#released under GNU GPL
import numpy as np

a = 8
b = 11
c = 13
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)
