''' time complexity O(n**2)'''
def insertion_sort(nums):
    for i in range(1,len(nums)):
        while i>0 and nums[i-1]>nums[i]:
            nums[i],nums[i-1] = nums[i-1],nums[i]
            i-=1
    return nums
print ('enter ur sequence of numbers with spaces between them')
s=[int(i) for i in input().split()]
print(insertion_sort(s))
