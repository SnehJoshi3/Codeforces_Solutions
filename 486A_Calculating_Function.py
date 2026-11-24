# Accepted Logic
a = int(input())
if a % 2 == 0:
    print(a // 2)
else:
    print(-(a + 1) // 2)

# Basic Logic
a = int(input())
s = 0
for i in range(1,a+1):
  if i % 2 == 1:
    s -= i
  else:
    s += i
print(s)
