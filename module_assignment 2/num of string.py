'''Write a Python program to count the number of characters (character
frequency) in a string'''


string = "hellohowareyou"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")


'''============================='''
#dictionary key(REMOVED ARE SAME AS TWO ALPHABET)
    
str = "hellohowareyou"

dict = {}

for i in str:

    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1
        
print(dict)
