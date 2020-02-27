""" count the number of even and odd numbers from a series of numbers"""

print("Enter the series of numbers: ")
num = input()
odd, even = 0, 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"The number of odd numbers is {odd}")
print(f"The number of even numbers is {even}")
