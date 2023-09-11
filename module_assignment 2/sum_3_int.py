'''Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.'''

num_1=int(input("enter a number"))
num_2=int(input("enter a number"))
num_3=int(input("enter a number"))
sum=0

if num_1==num_2==num_3:
    print(sum)
else:
    total=num_1+num_2+num_3
    sum=total
    print("the sum is equal",sum)
