n = int(input())
count = 0
for _ in range(n):
  row_list = list(map(int, input().split()))
  if sum(row_list)>=2:
    count += 1
print(count)
