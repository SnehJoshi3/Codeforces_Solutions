levels = int(input())
x = list(map(int, input().split()))[1:]  
y = list(map(int, input().split()))[1:]  
 
unique_levels = set(x + y)
 
if len(unique_levels) == levels:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
