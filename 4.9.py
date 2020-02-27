"""find factorial of a number"""


factr = []
num = int(input("Enter the num to find its factorial: "))
for i in range(1, num):
    if num % i == 0:
        factr.append(i)
print(f"The factorials of {num} are {factr}")
print()
