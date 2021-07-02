# Best problem on CodingBat- if we try to solve this without loops
def make_bricks(small, big, goal):
  if big <= goal // 5:
    return small >= goal - big * 5
  else:
    return goal % 5 <= small