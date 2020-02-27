"""Write a recursive Python function that returns the sum of first n integers"""


def sumFirstN(n, lim):
    if n >= lim:
        return n
    return n + sumFirstN(n + 1, lim)


lim = int(input('returns the sum of first n integers. Input the value of n: '))
print(sumFirstN(0, lim))

# print(sum([i for i in range(lim+1)]))
