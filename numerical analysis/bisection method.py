print('################bisection method#################')
''' bisection method is used to find the root of a func in [a,b]
u can also implement it in matlab'''
import math
def bisection(func,a,b):
    if func(a)==0:
        return a
    elif func(b)==0:
        return b
    elif func(a)*func(b)>0:# f(a).f(b) should always be less then 0
        print(' no root in [a,b]')
        return
    else:
        mid=(a+b)/2
        while abs(a-b)>10**-7: #here  10^-7 is tolerance
            if func(mid)==0:
                return mid
            elif func(mid)*func(a)<0:
                b=mid
            else:
                a=mid
            mid=(a+b)/2
    return mid
#==================================================================
def f(x):
    return math.pow(x, 3) - 2*x - 5

'''print('please input ur function in terms of x like 2*x - 5')
f=lambda x:input()'''#still working on it.
print('input ur limits with space')
s=[int(i) for i in input().split()]
if(len(s)==2):
    print(bisection(f,s[0],s[1]))
else:
    print('invalid input')

