'''Write a python program to sum of the first n positive integers.'''

#using for loop:

num = 5
sum = 0
for i in range(num+1):
  sum+=i
print(sum)

'''================================'''
#using while loop

num = int(input("Enter a number: "))  
  
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
    
   while(num > 0):  
       sum += num  
       num -= 1  
   print("The sum is",sum)  
