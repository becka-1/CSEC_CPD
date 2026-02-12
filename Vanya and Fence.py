n, h = map(int, input().split())
lst = list(map(int, input().split()))
count = n

for i in range(n):
  if lst[i] > h:
    count += 1

print(count)
  
