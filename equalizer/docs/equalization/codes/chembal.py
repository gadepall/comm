#Code by GVV Sharma
#Jan 21, 2020
#released under GNU GPL
#Balancing a chemical equation

import numpy as np
import sympy

#if using termux
import subprocess
import shlex
#end if

#Coefficient Matrix
A = np.array([[1,0,-3, 0],[0,2,0, -2],[0,1,-4, 0]]) 

#Row reduced echelon form
print(sympy.Matrix(A).rref())


