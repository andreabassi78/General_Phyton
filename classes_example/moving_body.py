import numpy as np
import matplotlib.pyplot as plt

pos = np.array((0.0,0.0))
vel = np.array((0.5,0.5))

ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

dt = 0.1
N = 30

for i in range(N):
    dr = vel * dt
    pos += dr
    x = pos[0]
    y = pos[1]
    ax.scatter(x, y, c = 'red')
    plt.pause(dt)

plt.show()

    
