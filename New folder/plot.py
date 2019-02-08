
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = Axes3D(fig) #fig.add_subplot(111, projection='3d')


x, y, z, intensity, photon_count = np.loadtxt('writefile.txt', delimiter=',', unpack=True)

"""X, Y = np.meshgrid(x, y)

Z = np.reshape(photon_count, X)
#Z = np.array(photon_count)
#Z = Z.reshape((1, 1)
#Z = photon_count
#Z=np.random.rand(len(Y),len(X))
plt.contour(X, Y, Z, colors='black')
plt.show()
"""



p = ax.scatter(x, y, z, c=photon_count, marker='o') #, c='r', marker='o'

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

fig.colorbar(p)

plt.show()