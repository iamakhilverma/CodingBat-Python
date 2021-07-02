def count_evens(nums):
  evens = 0
  for num in nums:
    if num % 2 == 0:
      evens += 1
  return evens