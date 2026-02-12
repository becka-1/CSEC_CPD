n = int(input())
count = 0

for i in range(n):
  lst = list(map(int, input().split()))

  if lst.count(1) >= 2:
    count += 1

print(count)
