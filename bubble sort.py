#it is kinda like merge sort
#but it is more simpler
#it checks the adjacent elements
def bubblesort(arr):
    n=len(arr)
    for i in range (n):                     #i starts from 1
        for j in range (0,n-i-1):            #j starts from zero
           if arr[j]>arr[j+1]:
              arr[j],arr[j+1]= arr[j+1],arr[j]  # it just moves the largest element 
    return arr                                  #on the right side 
arr=[int(i) for i in input().split()]
print(arr)
print(bubblesort(arr))


        
