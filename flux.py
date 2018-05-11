import numpy as np
import matplotlib as plt

class Electric_Field:

K = 8.9875517873681764 * (10**9) 
epsilon = 8.85418782/(10**12)

"""For 'shape', the user enters one of a variety of shapes of objects of some shape (i.e. infinite wire, wire,
sphere, etc. For x and y distance, the user enters either a specific distance or range of distances they want to measure the field from. For Q, the user enters the initial surface charge or charge density that is pertinent to the   shape he or she is looking at. For origin, the user enters the x-y coordinates as a list of where the field is goingto be measured from"""


    def _init_(self, shape, xdistance, ydistance, Q, origin):
        self.shape = shape
        self.xdistance = xdistance
        self.ydistance = ydistance
        self.Q = Q
        self.origin = origin

#This function assumes all shapes are situated parallel to the x-axis
    def field(self):
        xfield = 0
        yfield = 0
        if self.shape == 'point':
            xfield = (Q*K)/(xdistance**2) 
            yfield = (Q*K)/(ydistance**2)
        elif self.shape == 'infinit plane':
            xfield = 0
            yfield = Q/(2*epsilon)
        elif self.shape == 'infinite wire':
            xfield = 0
            yfield = Q/(2*np.pi*ydistance*epsilon)
        elif self.shape = 'sphere':
            xfield = (Q*K)/(xdistance**2)
            yfield = (Q*K)/(ydistance**2)
        elif self.shape = 

