# https://codeforces.com/problemset/problem/617/A
x = int(input())
moves = [5, 4, 3, 2, 1]

if x % 5 == 0:
    print(x // 5)
else:
    i = 1
    i += x // 5
    print(i)
