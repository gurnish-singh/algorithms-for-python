# this is a fairly good eaxample of dynamic programing where we compute
# the binomial coffecients using the pascals triangle
print('give input n and k respectively to find the binomial of {n/k}'
      ' where n>=k')
n,k=map(int,input().split())
def bin(n,k):
    if (k==0 or n==k):
        return 1
    elif k>n:
        return 'error'
    else:
        return bin(n-1,k-1)+bin(n-1,k)

print(bin(n,k))
