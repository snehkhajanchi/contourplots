from mpl_toolkits import mplot3d
# Then, to create a 3D axes you can execute this code:
<pre id="3346" class="graf graf--pre graf-after--p">%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection=’3d’)</pre>


def f(x, y):

    return np.sin(np.sqrt(x ** 2 + y ** 2))
    
    

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
 
X, Y = np.meshgrid(x, y)
Z = f(X, Y)fig = plt.figure()

ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');
