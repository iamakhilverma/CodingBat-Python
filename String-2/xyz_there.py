def xyz_there(str):
  for i in range((len(str) - 3), -1, -1):
    if str[i:i+3] == 'xyz':
      if i == 0:
        return True
      else:
        if str[i-1] == '.':
          return False
        else:
          return True
  return False