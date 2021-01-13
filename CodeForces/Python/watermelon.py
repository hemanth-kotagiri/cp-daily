# 1kg and 2kg and 3kg and 5kg... of watermelon output => NO
# conclusing: all odd numbers including 1 and 2 are :NO
w = int(input())
if 1 <= w <= 100:
    if w % 2 == 0 and w != 2:
        print("YES")
    else:
        print("NO")
