"""Check if passed string is palindrome or not"""


def isPalindrome(inS):
    S = inS.lower()
    if len(S) == 1 or len(S) == 0:
        return True
    if S[0] == S[-1]:
        middle = S[1: -1]
        return isPalindrome(middle)
    else:
        return False
