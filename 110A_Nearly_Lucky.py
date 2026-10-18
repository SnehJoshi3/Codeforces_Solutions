s = input()
lucky_digit_count = s.count('4') + s.count('7')
if lucky_digit_count == 4 or lucky_digit_count == 7:
    print("YES")
else:
    print("NO")
