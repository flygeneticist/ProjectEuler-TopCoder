# first part involved generating and storing the data on fib nums
import math

def nth_fib(n):
    return int((((1+math.sqrt(5.0))/2.0)**n)/math.sqrt(5.0)+0.5)


def fibs_to_file(limit):
    data = []
    with open('fib_data.txt','w') as data:
        for i in range(1,limit):
            dataline = str(i) + "," + str(len(str(nth_fib(i))))
            data.write(dataline + '\n')

# Now to work with the data to try and find patterns to exploit 
import matplotlib.pyplot as plt 

plt.plotfile('fib_data.txt', delimiter=',', cols=(0, 1), 
    names=('n-th Fibonaci Number', 'Length of n-th Fibonaci Number'))
plt.show() # length of Fib num appears to increase linearly where (1 <= n <= 1475)

# let's find the approximate slope of the line
def slope(ax,bx,d=data):
    ay = d[ax-1][1]
    by = d[bx-1][1]
    return ((by-ay)/(bx-ax))

# find the slope for several different snapshots of the data and avergage
from random import randint

def avg_slope(data_limit):
    slopes = []
    n = 1
    while n <= 50:
        # get a slope for two random n points and add to slope list 
        a = randint(0,data_limit)
        b = randint(0,data_limit)
        slopes.append(slope(a,b))
        n += 1
    return float(sum(slopes)/len(slopes))

# bootstrap the slope 1000 times to get a true average sampling of the slope of the line
def bootstrap(times):
    boot = []
    for i in range(times):
        boot.append(avg_slope(len(data)-1))
    return float(sum(boot)/len(boot))

print(bootstrap(1000))
