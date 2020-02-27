"""For given integer x,
    print ‘True’ if it is positive,
    print ‘False’ if it is negative and
    print ‘zero’ if it is 0"""

x = int(input("Enter a number: "))
if x > 0:
    print('positive')
elif x<0:
    print('negative')
else:
    print('zero')