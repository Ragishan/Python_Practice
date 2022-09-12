# Import the library

import matplotlib.pyplot as plt


# Create a class Circle

class Circle(object):
    
    # Constructor
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  

#Create an object from Circle Class

Redcircle = Circle(10,'red')

#Printing the radius and color attribute of the Circle Class using the object that we
#created i.e 'Redcircle'

print(Redcircle.radius)
print(Redcircle.color)

#Drawing the circle by calling the drawCircle method from the Circle Class
#that we have created above. Again we will use our Class obejct i.e Redcircle

Redcircle.drawCircle()

Bluecircle = Circle(5,"blue")

print(Bluecircle.radius)
print(Bluecircle.color)

Bluecircle.drawCircle()