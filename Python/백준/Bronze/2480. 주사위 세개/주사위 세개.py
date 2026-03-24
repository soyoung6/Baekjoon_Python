a, b, c = map(int, input().split())

if a == b == c:
  m1 = 10000+(a*1000)
  print(m1)
elif (a == b) or (b == c) or (a == c):
  if a == b:
    m2 = 1000 + (a*100)
  elif b == c:
    m2 = 1000 + (b*100)
  else:
    m2 = 1000 + (c*100)
  print(m2)
else: 
  d = max(a, b, c)
  m3 = d*100
  print(m3)