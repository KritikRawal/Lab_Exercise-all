""".Write a Python program that accepts a string and calculate the number of
digits and letters"""

print("Enter the string:")
ans = input()
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "num", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
numlet, numdig = 0, 0
for i in ans:
    if i in letters:
        numlet += 1
    elif i in digits:
        numdig += 1
print(f"{numdig} letters, {numlet} digits")
