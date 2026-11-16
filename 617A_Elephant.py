x = int(input())
steps = 0
while x > 0:
  x -= min(x,5)
  steps += 1
print(steps)
