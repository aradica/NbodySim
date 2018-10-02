import numpy as np
from itertools import combinations
from matplotlib import pyplot as plt

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
    def __init__(self, bodies, time, dx):
        self.bodies = bodies
        self.time = int(time/dx)
        self.dx = 86400*dx #n of seconds in a day, for easier input
        self.pairs = list(combinations(self.bodies, 2))

    def calculateForces(self):

        for body in self.bodies:
            body.force *= 0 #set to zero

        for body1, body2 in self.pairs:
            F = body1.Fg(body2) * body1.unitVector(body2)

            #Newton's Third Law
            body1.force += F
            body2.force -= F 


    #Add all forces and then move the bodies a little bit (errors don't cancel out - orbital drifts can and will occur!)
    def updateFrame(self):
        self.calculateForces()
        for body in self.bodies:
            axyz = body.force/body.mass
            vxyz = axyz*self.dx
            sxyz = (vxyz*self.dx)/2
        
            body.coordinates += body.velocity*self.dx + sxyz
            body.velocity += vxyz
    
    #TODO
    #def run(self):   

if __name__ == "__main__":
    Earth = Body("Earth", 5.97219e24, [150000000000, 0, 0], [0, 30000, 0])
    Sun = Body("Sun", 1.9891e30, [0, 0, 0], [0, 0, 0])

    time = int(input("T[days]: "))

    factor = float(input("dx[days]: "))

    x, y = [], []
    x2, y2 = [], []

    Cosmos = Simulator([Sun, Earth], time, factor)
    print("Total number of frames to compute:", Cosmos.time)
    for k in range(Cosmos.time):
        Cosmos.updateFrame()
        x.append(Earth.coordinates[0])
        y.append(Earth.coordinates[1])
        x2.append(Sun.coordinates[0])
        y2.append(Sun.coordinates[1])

    #plt.plot(list(range(test)), x)
    #plt.plot(list(range(test)), y)
    #print("---DONE---")
    #print(len(list(range(test))))
    #print(Earth)
    #plt.show()

    plt.scatter(x, y)
    plt.scatter(x2, y2)
    plt.show()
