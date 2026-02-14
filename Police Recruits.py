n = int(input())
events = list(map(int, input().split()))

crimes = 0
fOfficers = 0

for i in range(n):
  if events[i] == -1:
    if fOfficers > 0:
      fOfficers -= 1
    else:
      crimes += 1
  else:
    fOfficers += events[i]

print(crimes)
