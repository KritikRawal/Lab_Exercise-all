"""sum of three given integers.
    However, if two values are equal sum will be zero."""

num1 = int(input('enter the number:'))
num2 = int(input('enter the number:'))
num3 = int(input('enter the number:'))
sum = num1 + num2 + num3
if num1 == num2 or num1 == num3 or num2 == num3:
    print('sum is zero')
else:
    print('sum is', sum)
