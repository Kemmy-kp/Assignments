What is used to check whether an object o is an instance of class A?

In Python, you can use the isinstance() function to check whether an object is an instance of a particular class or a class derived from it. The isinstance() function takes
two arguments: the object you want to check and the class or tuple of classes you want to check against.

class A:
    pass

class B(A):
    pass

obj_a = A()
obj_b = B()

print(isinstance(obj_a, A))  # Output: True
print(isinstance(obj_b, A))  # Output: True
