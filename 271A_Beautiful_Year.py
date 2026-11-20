date = int(input())
while True:
  date += 1
  seen = set()
  for num in str(date):
    seen.add(num)

  if len(seen) == len(str(date)):
    print(date)
    break
