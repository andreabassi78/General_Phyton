

import numpy as np
import matplotlib.pyplot as plt

class Body:

    def __init__(self,pos,vel):
        self.pos = pos
        self.vel = vel
        plt.figure()
        self.ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

    def move(self,dt):
        self.pos = self.pos + self.vel*dt

    def show(self):
        x = self.pos[0]
        y = self.pos[1]
        self.ax.scatter(x, y, c = 'red')
        plt.pause(dt)

dt = 0.1
N = 30

my_first_body = Body(pos=np.array([0.0,0.0]), 
                     vel=np.array([0.5,0.5]))

my_second_body = Body(pos=np.array([0.1,0.1]), 
                     vel=np.array([0.2,-0.5]))

for i in range(N):
    my_first_body.move(dt)
    my_first_body.show()
    my_second_body.move(dt)
    my_second_body.show()


#plt.show()

    
