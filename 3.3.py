"""Write a function called showNumbers that takes a parameter called limit.
It should print all the numbers between 0 and limit,
with a label to identify the even and odd numbers."""


def showNumbers(limit):
    for i in range(0, limit + 1):

        if i % 2 == 0:
            print(str(i) + ":" + 'EVEN')


        else:

            print(str(i) + ":" + 'ODD')


limit = int(input("Give me a number. "))

showNumbers(limit)
