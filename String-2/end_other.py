def end_other(a, b):
  a = a.lower()
  b = b.lower()
  
  if len(a) < len(b):
    return a == b[(len(b) - len(a)):]
  elif len(a) > len(b):
    return a[(len(a) - len(b)):] == b
  else:
    return a == b