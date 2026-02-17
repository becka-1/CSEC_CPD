s = input()
t = input()

count = 1

x = 0
sCurrent = s[0]
tCurrent = t[0]

for i in range(len(t)):
  if sCurrent == tCurrent:
    count += 1
    x += 1
    sCurrent = s[x]
  if i < len(t)-1:
    tCurrent = t[i+1]

print(count)
