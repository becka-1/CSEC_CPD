s1 = input()
s2 = input()

x = s1.lower()
y = s2.lower()

if x < y:
  print(-1)
elif y < x:
  print(1)
else:
  print(0)
