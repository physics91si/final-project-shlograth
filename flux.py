from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class Field_Fun:
    """For 'shape', the user enters one of a variety of shapes of objects of some shape (i.e. infinite wire, wire,
    sphere, etc. For x and y distance, the user enters either a specific distance or range of distances they want to measure the    field from. For Q, the user enters the initial surface charge or charge density that is pertinent to the   shape he or she is       looking at. For origin, the user enters the x-y coordinates as a list of where the field is goingto be measured from"""

    #shape must be input as a string, origin must be input as a list with the first component as the x position and the second        #as the y position.
    def __init__(self, shape, xdistance, ydistance, Q, origin):
        self.shape = shape
        self.xdistance = xdistance
        self.ydistance = ydistance
        self.Q = Q
        self.origin = origin
        self.K = 8.9875517873681764 * (10**9)
        self.epsilon = 8.85418782/(10**12)
       
    #This part was written for my own convenience, and was almost entirely done by Kaitlyn when I came to her for help. Thank
    #you Kaitlyn.
    def point_charge(self, x, y):
        R = np.sqrt((self.xdistance - self.origin[0])**2 + (self.ydistance - self.origin[1])**2) + 1e-12
        Ex = self.Q*(x - self.origin[0])/R**2
        Ey = self.Q*(y - self.origin[1])/R**2
        return Ex, Ey
    
    #Again, this is a function made for my own convenience (it makes graphing easier)
    def infin_wire(self, x):
        Ex = x
        Ex = Ex * 0
        Ey = self.Q/(2 * np.pi * x * self.epsilon)
        return Ex, Ey
   
    #Again, convenience. Side Note: all of these functions simply help create an approximate vector field, not an exact on. The
    #real field is proportional to this one.
    def infin_plane(self, x):
        regulator = x/np.absolute(x)
        Ex = x
        Ex = Ex * 0
        Ey = (self.Q/(2 * np.pi)) * regulator
        return Ex, Ey
    
    #This function assumes all shapes are situated parallel to the x-axis, and returns exact values
    def field(self):
        xfield = 0
        yfield = 0
        if self.shape == 'point' or self.shape == 'shpere':
            xfield = (self.Q * self.K)/(self.xdistance**2)
            yfield = (self.Q * self.K)/(self.ydistance**2)
        elif self.shape == 'infinite plane':
            yfield = self.Q/(2 * self.epsilon)
        elif self.shape == 'infinite wire':
            yfield = self.Q/(2 * np.pi * self.ydistance * self.epsilon)
        #The origin of the parallel plate capacitor will be the center of the bottom plate, and the top plate will simply be
        #there so the graph looks easy on the eyes.
        elif self.shape == 'parallel plate capacitor':
            yfield = self.Q/self.epsilon
        return xfield, yfield

    #This function is used to find the potential difference for some range r1 to r2
    '''def potential(self):
        X, Y = self.field()
        xpotential = X * -1 * (self.xdistance - self.origin[0])
        ypotential = Y * -1 * (self.ydistance - self.origin[1])
        return xpotential, ypotential'''

    #This function will graph one of the types of fields that you want to make, where Efield is the electric field
    #Vfield is the potential graph.
    def graph_the_bitch(self):
        Xone = np.linspace((self.origin[0] + 1e-12) - self.xdistance, (self.origin[0] + 1e-12) + self.xdistance, 30)
        Yone = np.linspace((self.origin[1] + 1e-12) - self.ydistance, (self.origin[1] + 1e-12) + self.ydistance, 30)
        X, Y = np.meshgrid(Xone, Yone)
        U = 0
        V = 0
        if self.shape == 'point' or self.shape == 'sphere':
            U, V = self.point_charge(X, Y)
            U = U/np.sqrt(U**2 + V**2)
            V = V/np.sqrt(U**2 + V**2)
        #Below just add aditional lines to the graph to give you a sense of where the objects with electric field are with 
        #respect to the field vectors
            plt.quiver(X, Y, U, V)
            plt.scatter(self.origin[0], self.origin[1], marker='o')
        elif self.shape == 'infinite plane' or self.shape == 'infinite wire':
            U, V = self.infin_plane(Y)
            if self.shape == 'infinite wire':
                U, V = self.infin_wire(Y)
            plt.quiver(X, Y, U, V, angles='xy', scale_units='inches', scale = 20)
            x = np.linspace(-self.xdistance, self.xdistance, self.xdistance * 50)
            y = np.full(self.xdistance * 50, self.origin[1])
            plt.plot(x, y, c='red')
        plt.xlim((self.origin[0] - self.xdistance, self.xdistance + self.origin[0]))         
        plt.ylim((self.origin[1] - self.ydistance, self.ydistance + self.origin[1]))
        plt.show()
        
