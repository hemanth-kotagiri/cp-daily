n = int(input())
i=0
count=0
while i<n:
    now = [int(i) for i in input().split(" ")]
    if now.count(1)>1:
        count+=1
    i+=1
print(count)