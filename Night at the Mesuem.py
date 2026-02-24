s = input()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

x = 0

count = 0

for i in range(len(s)):

  p = abs(letters.index(letters[x]) - letters.index(s[i]))

  count += min(p, abs(26 - p))

  x = letters.index(s[i])
  
print(count)
