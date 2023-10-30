#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


my_rectangle = Rectangle(5, 4)


area_of_my_rectangle = my_rectangle.area()

print(f"The area of the rectangle is: {area_of_my_rectangle} square units")  
