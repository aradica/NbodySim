import numpy as np
from itertools import combinations
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import datetime
import os
import json

class Body:

    def __init__(self, name, mass, coordinates, velocity):
        self.name = name
        self.mass = mass
        self.coordinates = np.array(coordinates, dtype=float) #xyz coordinates
        self.velocity = np.array(velocity, dtype=float) #xyz velocities

        self.force = np.array([0.0, 0.0, 0.0], dtype=float)

    def __repr__(self):
        return "Body '{}' at {} going {} m/s.".format(self.name, self.coordinates, self.velocity)

    def Fg(self, other):
        #F = G*m1*m2*/d^2
        return (6.674e-11 * self.mass * other.mass)/np.sum(np.square(self.coordinates - other.coordinates))

    def Distance(self, other):
        return np.sqrt(np.sum(np.square(self.coordinates - other.coordinates)))

    def unitVector(self, other):
        return (other.coordinates - self.coordinates)/self.Distance(other)


#O(n) = n^2, Euler integration
#TODO: leapfrog, Barnes-Hut...
class Simulator: 
    def __init__(self, bodies, time, dx, unit=86400):
        self.bodies = bodies
        self.time = int(time/dx)
        self.dx = unit*dx #n of seconds in a day, for easier input
        self.pairs = list(combinations(self.bodies, 2))

    def calculateForces(self):
        for body in self.bodies:
            body.force *= 0 #set to zero

        for body1, body2 in self.pairs:
            F = body1.Fg(body2) * body1.unitVector(body2)

            #Newton's Third Law
            body1.force += F
            body2.force -= F 

    
    #returns dictionary (JSON, anyone?)
    def simulate(self):
        sim = {k.name : [] for k in self.bodies}
        for t in range(self.time):
            self.calculateForces()

            #Add all forces and then move the bodies a little bit (errors don't cancel out - orbital drifts can and will occur!)
            for body in self.bodies:
                axyz = body.force/body.mass
                vxyz = axyz*self.dx
                sxyz = (vxyz*self.dx)/2
            
                body.coordinates += body.velocity*self.dx + sxyz
                body.velocity += vxyz #TODO why not append coordinates here? MERGE updateFrame() and simulate()!
                sim[body.name].append(list(body.coordinates)) #without list() all numbers are the same???
    
        return sim


def FastPlot2D(sim, ax1=0, ax2=1):
    fig, ax = plt.subplots()
    for body in sim:
        xyz = np.asarray(sim[body])
        x, y  = xyz[:,ax1], xyz[:,ax2]
        ax.scatter(x, y, label=body)
    plt.title("N body simulation")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    ax.legend(loc='best')
    plt.show()


def FastPlot3D(sim, boundary, colors, save=0, pause=0.01):
    frames = []
    for body in sim:
        xyz = np.asarray(sim[body])
        x, y, z  = xyz[:,0], xyz[:,1], xyz[:,2]
        frames.append([x, y, z])

    frames = np.asarray(frames).T

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    if save == 1:
        os.makedirs("3d "+timestamp)

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    bx, by, bz = boundary[0], boundary[1], boundary[2]
    for t, frame in enumerate(frames):
        #ax.autoscale(False)
        #                                    check this first if errors start to occur!                            
        f1, f2, f3 = frame
        ax = plt.gca()
        ax.set_xlim(bx)
        ax.set_ylim(by)
        ax.set_zlim(bz)

        ax.scatter(f1, f2, f3, alpha = 1, c=colors)
        plt.title("Frame {}".format(t))
        
        plt.draw()
        if save == 1:
            plt.savefig("3d "+timestamp+"/"+str(t)+".png")

        plt.pause(pause)
        ax.cla()   


def LoadSimTask(file):
    with open(file) as f:
        data = json.load(f)
    d = data["bodies"]
    b = [Body(body, d[body]["mass"], d[body]["coordinates"], d[body]["velocity"]) for body in d]
    return Simulator(b, data["time"], data["dx"], unit=data["factor"])
    


if __name__ == "__main__":
    """
    Earth = Body("Earth", 5.97219e24, [150000000000, 0, 0], [0, 30000, 0])
    Sun = Body("Sun", 1.9891e30, [0, 0, 0], [0, 0, 0])

    print("*Default unit are in days")
    time = int(input("Time: "))
    dx = float(input("dx: "))

    Cosmos = Simulator([Earth, Sun], time, dx)
    """

    Cosmos = LoadSimTask("example.json")
    c = Cosmos.simulate()
    #FastPlot2D(c)
    box = [[-3e11, 3e11], [-3e11, 3e11], [-3e11, 3e11]]
    FastPlot3D(c, box, colors=[0, 1 , 2, 5], save=1)