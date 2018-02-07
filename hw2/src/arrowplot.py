# astr5400/src/arrowplot.py
#
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#

import matplotlib.pyplot as plt
import numpy as np

X, Y = np.meshgrid(np.arange(-5,5,1.0),np.arange(-5,5,1.0))
U = Y
V = -X

plt.figure()
plt.title('Arrowplot with vortices in opposite directions')
Q = plt.quiver(X,Y,U,V,units='width',color='red')
U = -Y
V = X
Q1 = plt.quiver(X+5,Y,U,V,units='width',color='blue')

plt.show()
