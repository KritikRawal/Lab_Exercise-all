"""display the Fibonacci series between 0 and 50"""
disp = 0
a = 1
series = []
while disp <= 50:
    series.append(disp)
    temp = disp
    disp = disp + a
    a = temp
print(series)