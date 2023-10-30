#Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


my_circle = Circle(5)


circle_area = my_circle.area()
circle_perimeter = my_circle.perimeter()

print(f"The area of the circle is: {circle_area:.2f} square units")
print(f"The perimeter of the circle is: {circle_perimeter:.2f} units")
