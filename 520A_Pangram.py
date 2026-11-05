x = int(input())
sentence = input()
if len(set(sentence.lower())) >=26:
  print("YES")
else:
  print("NO")
