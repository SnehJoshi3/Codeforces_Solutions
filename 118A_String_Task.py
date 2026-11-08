text = input()
text = text.lower()
vowels = 'AIEOUYaieouy'
ans = ''
for c in text :
  if c not in vowels :
    ans += '.' + c
print(ans)
