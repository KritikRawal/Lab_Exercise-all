"""Write a recursive function that check if the given string is palindrome, else not
palindrome"""

def palindromeStr(strCheck, i, revString):
    if i < 0:
        if revString == strCheck:
            return 'palindrome'
        else:
            return 'Not a palindrome'
    revString += strCheck[i]
    return palindromeStr(strCheck, i-1, revString)

given = input('Enter a string to check for palindrome property: ')
print(palindromeStr(given, len(given)-1, ''))


