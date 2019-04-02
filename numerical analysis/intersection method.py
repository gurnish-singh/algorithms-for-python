#==========================intersection method============================
# to find roots between a and b
import math
def intersection(func,a,b):
    while 1:
        c=b-((func(b)*(b-a)))/(func(b)-func(a))
        if abs(c-b) < 10**-5:
             return c
        a=b
        b=c
#=========================================================
def f(x):
    return math.pow(x,3)-2*x-5
print('input ur limits with space')
s=[float(i) for i in input().split()]
if(len(s)==2):
    print(intersection(f,s[0],s[1]))
else:
    print('invalid input')
