n = int(input())
birds = list(map(int, input().split()))

m = int(input())

for i in range(m):
  shot = list(map(int, input().split()))
  shot = [shot[0]-1, shot[1]-1]

  x = birds[shot[0]] - 1
  y = x - shot[1]
  z = x - y

  if shot[0] > 0:
    birds[shot[0] - 1] += z
  
  if shot[0] < n - 1:
    birds[shot[0] + 1] += y
    
  birds[shot[0]] = 0

for bird in birds:
  print(bird)
