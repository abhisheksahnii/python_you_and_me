'''
Program to swap
'''

def swap(x, y):
    x, y = y, x
    return x, y

word1 = input("Enter first letter: ")
word2 = input("Enter second letter: ")

print("Swapping two numbers:",swap(word1, word2))
