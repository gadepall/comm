#Code by GVV Sharma
#March 14, 2019
#released under GNU GPL
import numpy as np

def linspace(first,last,k):
  t= np.zeros((k,1))
  t[0]=first
  d = (last-first)/(k-1)
  for n in range(2,k):
    t[n-1] = t[0]+(n-1)*d
  return t

x = np.linspace(-2,8,20)
print(x)
