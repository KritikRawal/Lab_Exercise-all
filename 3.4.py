"""Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). """


def summult(limit):
    summ = 0
    for i in range(limit + 1):
        if i % 3 == 0 or i % 5 == 0:
            summ = summ + i
    print()
    return summ
