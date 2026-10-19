x = int(input())
num = 0
for i in range(x):
  s = input()
  if '+' in s:
    num+= 1
  else: 
    num-=1
print(num)
