n = int(input())
i=0
x=0
while i<n:
    statement = input()
    if "+" in statement:
        x+=1
    else:
        x-=1
    i+=1
print(x)

