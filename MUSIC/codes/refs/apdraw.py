#Code by GVV Sharma
#March 15, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

x = np.loadtxt('ap.dat',dtype='float')
y1 = 8-x
y2 = 3*x-12

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# Major ticks every 2, minor ticks every 1
major_ticks = np.arange(-10, 10, 2)
minor_ticks = np.arange(-10, 10, 1)

ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)


# If you want different settings for the grids:
ax.grid(which='minor', alpha=0.2)
ax.grid(which='major', alpha=0.5)

#Plotting all lines
ax.plot(x,y1,label='$y_1$')
ax.plot(x,y2,label='$y_2$')


plt.xlabel('$x$')
plt.ylabel('$y$')
ax.legend(loc='best')

#if using termux
plt.savefig('../figs/draw_line.pdf')
plt.savefig('../figs/draw_line.eps')
subprocess.run(shlex.split("termux-open ../figs/draw_line.pdf"))
#else
#plt.show()







