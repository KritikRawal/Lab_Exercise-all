"""Write a function showstars(rows) to display a line of "*"
with an extra * each row
with parameter row to determine the number of rows of stars"""

rows=5
def showstars(rows):
    star = ""
    for i in range(rows):
        star = star + "*"
        print(star)
    print()

showstars(rows)