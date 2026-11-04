word = input()
upper = len([s for s in word if s.isupper()])
lower = len([s for s in word if s.islower()])
if upper > lower:
  print(word.upper())
elif lower > upper or lower == upper:
  print(word.lower())
