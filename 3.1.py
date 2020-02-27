"""to find the Max of three numbers """


def maxnum(a, b, c):
    if a >= b and a >= c:
        num = a
    elif b >= a and b >= c:
        num = b
    else:
        num = c
    print("Maximum number is ", num)


a = int(input('enter the number:'))
b = int(input('enter the number:'))
c = int(input('enter the number:'))
maxnum(a,b,c)