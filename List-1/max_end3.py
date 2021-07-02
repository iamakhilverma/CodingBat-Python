def max_end3(nums):
  if nums[0] > nums[-1]:
    return len(nums) * [nums[0]]
  return len(nums) * [nums[-1]]