lst = list(map(int, input().split()))
s = input()

count = 0

for i in range(len(s)):
  count += lst[int(s[i])-1]

print(count)
