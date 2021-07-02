def combo_string(a, b):
  if len(a) == 0 or len(b) == 0:
    return a+b
  if len(a) < len(b):
    return a+b+a
  elif len(a) > len(b):
    return b+a+b