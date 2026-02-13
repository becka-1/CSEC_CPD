s = input()
l = 0
u = 0

for i in range(len(s)):
  x = s[i].lower()
  if x == s[i]:
    l += 1
  else:
    u += 1

if l > u:
  print(s.lower())
elif l < u:
  print(s.upper())
else:
  print(s.lower())
