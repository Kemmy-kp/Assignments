#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


my_circle = Circle(3)

area_of_my_circle = my_circle.area()
perimeter_of_my_circle = my_circle.perimeter()

print(f"The area of the circle is: {area_of_my_circle:.2f} square units")
print(f"The perimeter of the circle is: {perimeter_of_my_circle:.2f} units")
