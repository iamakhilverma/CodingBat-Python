def sum13(nums):
  if not nums:
    return 0
  else:
    if 13 not in nums:
      return sum(nums)
    else:
      index = nums.index(13)
      return sum13(nums[:index] + nums[index+2:])
  
# def sum13(nums, i=0):
#   #exit condition
#   if(len(nums) == i):
#     return 0
#   if nums[i] == 13:
#     l = len(nums) - 1
#     return sum13(nums, i + (1 if i == l else 2))
#   return nums[i] + sum13(nums, i + 1)