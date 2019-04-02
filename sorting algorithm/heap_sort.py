#python progarma for heap sort
#average case performance=O(nlog(n))
'''
n=size of heap
create and maintain the heap using heapify
This is an implementation of max-heap, so after bullding the heap,
the max element is at the top 
We move it to the end of the list, which will later become the sorted list.
After moving this element to the end, we take the element in the end to the top
and shift it down to its right location in the heap.
We proceed to do the same for all elements in the heap,
such that in the end we're left with the sorted list.'''
def heapify(nums,n,i):
    largest=i # it is the root(parent)
    l=2*i+1#odd-------left---|  childs
    r=2*i+2#even------right--|
    #left child is always greater then the parent
    #and right child is always lesse then the parent
    # See if left child of root exists and is 
    # greater than root 
    if l<n and nums[i]<nums[l]:
        largest=l
        #similarly
    if r<n and nums[largest]<nums[r]:
        largest=r
    if largest!=i:
        nums[i],nums[largest]=nums[largest],nums[i] #swap
        heapify(nums,n,largest)
    
#sorting function
def heapsort(nums):
    n=len(nums)
    #build a maxheap
    for i in range (n//2-1,-1,-1):# from n to 0 that is hapify for every element
        heapify(nums,n,i)
    for i in range(n-1,0,-1):#from n-1 to 1
        nums[i],nums[0]=nums[0],nums[i] # swap
        heapify(nums,i,0)
    return nums
print('enter ur sequence of numbers with spaces')
s=[int(i) for i in input().split()]
print(heapsort(s))





        
    
