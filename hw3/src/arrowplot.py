# astr5400/src/arrowplot.py
#
# Omkar H. Ramachandran
# omkar.ramachandran@colorado.edu
#

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2.5,2.5,101)
y = np.linspace(-2.5,2.5,101)
X,Y = np.meshgrid(x,y)
R = (X**2+Y**2)**0.5
ii = np.where(R < 1)
R[ii] = 1.0
Th = np.arctan(Y/X)
Ur = 2*(1-1/R**2)*np.cos(Th)
Uth = -2*(1+1/R**2)*np.sin(Th)+10./2./np.pi/R
Ur[ii] = 0.0
Uth[ii] = 0.0
U = Ur*np.cos(Th) - Uth*np.sin(Th)
V = Ur*np.sin(Th) + Uth*np.cos(Th)

plt.figure()
plt.title('Arrowplot of flow field')
Q = plt.streamplot(X,Y,U,V,color='red')

plt.show()
