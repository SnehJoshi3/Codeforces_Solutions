from collections import Counter
n = int(input())
c = Counter(map(int, input().split()))
 
ans = c[4] + c[3] + c[2] // 2
c[1] = max(0, c[1] - c[3])  
 
if c[2] % 2:
  ans += 1
  c[1] = max(0, c[1] - 2)
  
ans += (c[1] + 3) // 4
 
print(ans)
