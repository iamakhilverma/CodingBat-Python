def front_times(str, n):
  if len(str) < 3:
    return n * str
  return n * str[:3]