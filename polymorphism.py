# polymorphism
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
# shapes = [Circle(5), Rectangle(4, 6)]
# for shape in shapes:
#     print("Area:", shape.area())
circle1= Circle(20)
print("Area of Circle:", circle1.area())
rectangle1= Rectangle(12,8)
print("Area of Rectangle:", rectangle1.area())
# In this example, we have a base class Shape with a method area(). 
# The Circle and Rectangle classes inherit from Shape and provide their own implementations of the area() method. 
# When we call the area() method on each shape object, the appropriate method is invoked based on the object's type, demonstrating polymorphism.

# child class of triangle and calculating area
class Triangle(Shape):
    def __init__(self, base, height):  # constructor with parameters
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
triangle1= Triangle(10,5)
print("Area of Triangle:", triangle1.area())