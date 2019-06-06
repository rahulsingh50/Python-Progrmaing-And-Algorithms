# Class: blueprint for creating new objects
# Objects: Instance of a Class
# Every Class function has at least one parameter called self.
# self is  reference of current object of class.python internally create the object in memory and set he reference of object in self 
# Class object have the bunch  of methods,normal,magic or  inherited from other classes.
# Class object has attributes genrally called variables.
# Class  has related methods and variable or attributes .
# Attributes are two types: Class label attributes and Instance label attributes
# Class label attributes visible or access across the all classes instencess.
# Class label attributes access two way using the class name and object name
# class label attributes changes in objects side not reflect in all classes instaness.
# we also create run time attributes of the objects
# instance vs class attributes
# We all time not define the attributes in constructore ,we define when we need or dynamic or run time ex.point.z =10

class Point:
    default_color = 'red'
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point is ({self.x},{self.y})")
    
point = Point(1,2)
print(point.draw())
print(Point.default_color)
print(point.default_color)
point.default_color = 'yellow' # change the class label attributes but changes reflect  current objects
print(Point.default_color)
print(point.default_color)
point.z = 10    # run time attribute creation or dynamic
print(point.z)
