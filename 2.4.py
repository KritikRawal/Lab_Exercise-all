"""Given three integers,
   print the smallest one.
   (Three integers should be user input)"""

num1=int(input('enter the number:'))
num2=int(input('enter the number:'))
num3=int(input('enter the number:'))
if num1<num2<num3:
    print('num1 is smallest one ')
elif num2<num1<num3:
    print('num2 is smallest one')
else:
    print('num3 is smallest')