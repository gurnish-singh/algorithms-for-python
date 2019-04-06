import numpy as np
n=int(input('eneter n'))
a=[]
l=[]
m=[]
a=np.zeros((n,n))
l=np.zeros((n,n))
m=np.zeros((n,n))
for i in range (n):
    for j in range (n):
        a[i,j]=input('enter the value of matrix at position'+repr(i)+','+repr(j))
print (a)
for i in range(n):
    l[i,i]=1
print(l)
for i in range (n-1):
    for j in range (i+1,n):
        m[j,i]=a[j,i]/a[i,i]
        l[j,i]=m[j,i]
        for k in range (n):
            a[j,k]=a[j,k]-m[j,i]*a[i,k]
u=np.dot(l,a)
print(l)
print(a)
print(u)

