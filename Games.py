n = int(input())

games = []
for i in range(n):
  game = list(map(int, input().split()))
  games.append(game)

count = 0

for i in range(n):
  for j in range(n):
    if games[i][0] == games[j][1]:
      count += 1
    if games[i][1] == games[j][0]:
      count += 1

print(count//2)
