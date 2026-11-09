p = int(input())
numbers = list(map(int, input().split()))
if numbers.count(1) > 0 :
  print("HARD")
else :
  print("EASY")
