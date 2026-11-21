k,n,w = map(int, input().split())
sum = k * w * (w + 1) // 2
print(max(0,sum -n))
