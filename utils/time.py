def convert_time(sec):
  s = sec % 60
  m = sec // 60
  h = 0
  if m > 60:
    h = sec // 3600
    m = m % 60
  time = f"{convert_timer(h)}:{convert_timer(m)}:{convert_timer(s)}"  
  return time

def convert_timer(s):
  if s < 10:
    return f"0{s}"
  return s