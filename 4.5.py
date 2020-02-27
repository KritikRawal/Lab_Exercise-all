"""accepts a word from user and reverses it"""
print("Enter the word to be reversed")
word = input()
rev = ""
for i in word:
    rev = i + rev
print(rev)