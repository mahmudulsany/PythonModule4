import random

random_points= int(input("Enter the number of random points: "))
radius= 1

N= random_points
n=0
loop=0
while loop<N:
    x= random.uniform(-1,1)
    y= random.uniform(-1,1)

    if (x**2 + y**2)<1:
        n=n+1
    loop=loop+1
print(f"The approximate value of pi is: {4*n/N}")
