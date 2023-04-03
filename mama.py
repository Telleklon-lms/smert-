import math
from math import sqrt
a = int(input())
b = int(input())
c = int(input())
P = a+b+c
p = 0.5*(a+b+c)
def per():
    print(a+b+c)
def s():
    print(math.sqrt(p*(p-a)*(p-b)*(p-c)))

per()
s()