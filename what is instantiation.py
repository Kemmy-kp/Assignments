What is Instantiation in terms of OOP terminology?

In object-oriented programming (OOP), instantiation is the process of creating an instance or an object of a class. An instance is a concrete realization of a class, and it is
used to represent and work with individual objects in your program.

Here's how the process of instantiation works:

Class Definition: First, you define a class, which serves as a blueprint or template for creating objects.
The class specifies the attributes (data) and methods (functions) that the objects of that class will have.

Creating an Instance: When you want to use the class to work with specific objects, you create an instance of that class. This process is often referred to as "instantiation."
When you instantiate a class, you are essentially creating an object based on the class's blueprint.

Object Initialization: The class may have an __init__ method, which is a special method that is automatically called when an instance of the class is created.
This method is used to initialize the attributes of the object. You can provide initial values for the object's attributes during instantiation.


ex:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)


