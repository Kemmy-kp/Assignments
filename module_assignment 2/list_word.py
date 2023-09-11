'''Write a Python function that takes a list of words and returns the length
of the longest one.'''

word_list = input("Enter a list of words: ").split()

max_length = 0

for word in word_list:
    if len(word) > max_length:
        max_length = len(word)

print("Length of the longest word:", max_length)
