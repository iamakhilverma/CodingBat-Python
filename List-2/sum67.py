# Recursive solution
def sum67(nums):
  def rem67(nums):
    if 6 not in nums:
      return nums
    index6 = nums.index(6)
    index7 = nums[index6:].index(7) + index6
    nums = nums[:index6] + nums[(index7 + 1):]
    return rem67(nums)
  return sum(rem67(nums))
  
# Elegant solution found on stack overflow
# def sum67(nums):
#   flag = True
#   sum = 0
#   for i in range(len(nums)):
#     if nums[i] == 6:
#       flag = False
#     if flag:
#       sum += nums[i]
#     if nums[i] == 7:
#       flag = True
#   return sum