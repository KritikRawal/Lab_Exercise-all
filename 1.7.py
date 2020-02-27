"""You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph;
then run the next two at15mph; before jogging the last at 7mph again. Will this be quicker or slower than the bus?"""

#time taken for bus to reach the journey
a=4
t1=(a//0.41)+20
print("The time taken by the bus to reach the journey is:",t1)

#time taken for boy to reach the journey
t2=a//0.47
print("The time taken by the boy to reach the journey is:",t2)

#comparing which one is faster
if t1<t2:
    print("Bus is quicker than a boy:")
else:
    print("Boy is quicker than bus")