"""Write a Python program to count the number of strings where the string length is 2
or more and the first and last character are same from a given list of strings."""

def reverse(string):
    reversedString = ""
    index = len(string)
    while index > 0:
        reversedString += string[index - 1]
        index = index - 1
    return reversedString

word = input("Enter a word")
print(reverse(word))