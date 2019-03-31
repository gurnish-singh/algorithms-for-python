# binary serach search for a given number in the sorted array
# in this example a non decreasing aray
print('enter a non decreasing sequence of numbers with spaces')
s=[int(i) for i in input().split()]
n=len(s)
print('enter the number to search')
a=int(input())
def location(x,low,high):
    if(s[low]>s[high]):
        return 0
    else :
        mid=(low+high)//2
        if(x==s[mid]):
            return mid+1
        elif x<s[mid]:
            return location(x,low,mid-1)+1
        else:
            return location(x,mid+1,high)+1
print(location(a,0,n-1))

