"""Write a Python program to display the multiplication of 3 upto n number using recursion."""

def tableMultiplication(n, lim):
    if n > lim:
        return "Completed"
    for i in range(1, 11):
        print(f'{n} x {i} = {n * i}')
    print('=====================')
    return tableMultiplication(n+1, lim)

lim = int(input('Python program to display the multiplication of 3 upto n number. Input the value of n: '))
print(tableMultiplication(3, lim))




