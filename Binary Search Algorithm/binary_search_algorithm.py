nums=[1,2,3,5,7,9,12,13,21,24,26,29,32,33,40,42,49]
def binary_search(left,right,res,nums):
    if right<left:
        return -1
    mid=(left+right)//2
    if nums[mid]<res:
        left=mid+1
        return binary_search(left,right,res,nums)
    elif nums[mid]>res:
        right=mid-1
        return binary_search(left, right, res, nums)
    elif nums[mid]==res:
        return mid
    return -1
s=binary_search(0,len(nums)-1,2,nums)
print(s)