def quick_sort(nums):
    if len(nums)<=1:
        return nums
    else:
        pivot=nums[0]
        greater=[int(i) for i in nums[1:] if i>pivot]
        lesser=[int(i) for i in nums[1:] if i<=pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
print('enter ur series of nums with spaces between them')
s=[int(i) for i in input().split()]
print(quick_sort(s))
