n = int(input())

count = 1
x = input()

for i in range(n-1):
  y = input()

  if x != y:
    count += 1
  x = y
  
print(count)
