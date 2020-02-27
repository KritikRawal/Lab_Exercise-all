"""Write a Python program to guess a number between 1 to 9. """
import random

num = random.randrange(10)
ans = 11
while ans!= num:
    print("Enter a random number: ")
    ans = int(input())
print("Well Guessed!")