"""Given a three-digit number
Find the sum of its digits."""

print("Enter a three- digit number")
a = int(input())
# separate number into digits
num = str(a)
x = num[0]
y = num[1]
z = num[2]
Sum = x + y + z
print('the sum is ',Sum)
