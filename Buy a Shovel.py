k, r = map(int, input().split())

x = 1

while (k * x) % 10 != 0 and str(k * x)[-1] != str(r):
  x += 1

print(x)
