def alarm_clock(day, vacation):
  if vacation:
    if day >= 1 and day <= 5:
      return '10:00'
    elif day == 0 or day == 6:
      return 'off'
  else:
    if day >= 1 and day <= 5:
      return '7:00'
    elif day == 0 or day == 6:
      return '10:00'