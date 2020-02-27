"""WAP which accepts marks of four subjects and
    display total marks, percentage and grade."""

"""Hint: more than 70% –> distinction,
    more than 60% –> first,d
    more than 40% –> pass,
    less than 40% –> fail"""

m=int(input('enter the marks in mathematics'))
n=int(input('enter the marks in nepali'))
s=int(input('enter the marks in social'))
p=int(input('enter the marks in physics'))

t=m+n+s+p
per=(t/400)*100
print('the total marks is',t)
if per>80:
    print('Distinction ')
    print('A+')
elif per>60<80:
    print('First Division')
    print('A')
elif per>50<60:
    print('Second Division')
    print('B+')
else:
    print('Fail')




