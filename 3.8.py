"""takes a number as a parameter and check the number is prime or not"""


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True


print('Start')
val = int(input('Enter the number to check prime:\n'))
ans = is_prime(val)
if ans:
    print(val, 'Is a prime number:')
else:
    print(val, 'Is not a prime number:')
