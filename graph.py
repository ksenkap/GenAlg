import numpy as np
import matplotlib.pyplot as plt
def function(x):
    return 8*x[0]**2+4*x[0]*x[1]+5*x[1]**2

x=np.linspace(-50, 50, 100)
y=np.linspace(-50, 50, 100)
X, Y = np.meshgrid(x, y)
Z = function([X, Y])

fig = plt.figure()

ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='green')
ax.set_title('График функции')
plt.show()


