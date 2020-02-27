"""Write a recursive program to check if the number is palindrome or not."""

def palindromeNum(numCheck, i, revNum):
    if i < 0:
        if revNum == numCheck:
            return 'palindrome'
        else:
            return 'Not a palindrome'
    revNum += numCheck[i]  
    return palindromeNum(numCheck, i-1, revNum)

given = input('Enter numbers to check for palindrome property: ')
print(palindromeNum(given, len(given)-1, ''))