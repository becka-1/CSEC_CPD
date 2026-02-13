n = int(input())
cards = list(map(int, input().split()))

scoreS = 0
scoreD = 0

while len(cards) > 0:
  scoreS += max(cards[0], cards[-1])
  cards.pop(cards.index(max(cards[0], cards[-1])))
  if len(cards) > 0:
    scoreD += max(cards[0], cards[-1])
    cards.pop(cards.index(max(cards[0], cards[-1])))

print(scoreS, scoreD)
