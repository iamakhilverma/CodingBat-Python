def last2(str):
  # return str.count(str[-2:]) - 1
  count = 0
  if len(str) < 2:
    return 0
  for i in range(len(str) - 1):
    if str[i:i+2] == str[-2:]:
      count += 1
  return count - 1