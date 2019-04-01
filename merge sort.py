''' python implementation of merge sort algorithm
best case complexity O(n)
worst case complexity O(n)'''
def merge_sort(nums):
    start=[]
    end=[]
    while len(nums)>1:
        a=min(nums)
        b=max(nums)
        start.append(a)
        end.append(b)
        nums.remove(a)
        nums.remove(b)
    if nums:
        start.append(nums[0])
    end.reverse()
    return (start+end)
print(' enter your sequence of numbers to sort')
s=[int(i) for i in input().split()]
print(merge_sort(s))
