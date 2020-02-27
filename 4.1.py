"""Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between
1500 and 2700 (both included).  """
print()
num = []
for i in range(1500, 2700 + 1):
    if i % 7 == 0 and i % 5 == 0:
        num.append(i)
print(f" Numbers between 1500 and 2700 (both included) that are divisible by both 7 and 5 are: ")
print(num)
print()
