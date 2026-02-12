mtrx = []
for i in range(5):
  row = list(map(int, input().split()))
  mtrx.append(row)

center = [3, 3] 
position = []

for i in range(5):
  for j in range(5):
    if mtrx[i][j] == 1:
      position.append(i+1)
      position.append(j+1)
      break

ans = abs(center[0] - position[0]) + abs(center[0] - position[1])
print(ans)
