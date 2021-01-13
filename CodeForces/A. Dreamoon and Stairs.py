from math import ceil
n,m = input().split(" ")
n,m = int(n),int(m)
steps = 0
if n<m:
    print(-1)
    exit()
elif n==m:
    steps = ceil(n/2)
    if steps%m==0:
        print(steps)
    else:
        print(-1)
    exit()
else:
    while n!=0:
        n=n-2
        steps+=1
        if n==2 or n==1:
            break
    if n==2:
        steps+=2
    if n==1:
        steps+=1

if steps%m==0:
    print(steps)
else:
    print(-1)


