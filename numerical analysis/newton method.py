#newtons method for fnding roots
#func1 is the diffentiated function of func with respect to x
def newton(func,func1,x):
    while True:
        y=x-func(x)/func1(x) #formula
        if abs(y-x)<10**-5:#tolerence conidtion
            return y
        x=y
def f(x):
    return (x**3) - (2 * x) -5

def f1(x):
    return 3 * (x**2) -2
print(newton(f,f1,3))
