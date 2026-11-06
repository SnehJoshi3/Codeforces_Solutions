fl = input()
fl = fl.split(' ')
n = int(fl[0])
k= int(fl[1])
sl = input()
scores = sl.split(' ')
target_score = int(scores[k - 1])
count = 0
for i in range(n):
    current_score = int(scores[i])
    if current_score >= target_score and current_score > 0:
        count += 1
print(count)
