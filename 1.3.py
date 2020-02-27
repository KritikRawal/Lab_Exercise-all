"""N students take K apples and distribute them among each other evenly
   The remaining (the undivisible) part remains in the basket
   How many apples will each single student get?
   How many apples will remain in the basket?
   The program reads the numbers N and K
   It should print the two answers for the questions above"""

n = int(input("Number of students: "))
k = int(input("Number of apples: "))
# after distributing them evenly
remain = k % n
each = k // n
print('the remaining apple is',remain)
print('each apples students get',each)
