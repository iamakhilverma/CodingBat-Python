def make_chocolate(small, big, goal):
  if goal % 5 == 0 and big >= goal // 5:
    return 0
  if big <= goal // 5:
    if small >= goal - big * 5:
      return goal - big * 5
    return -1
  else:
    if small >= goal % 5:
      return goal % 5
    else:
      return -1