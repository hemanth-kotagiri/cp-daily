def gcd(a,b):
    gcd = 0
    x =0
    while True:
        x = a%b
        a,b=b,x
        if(x==1):
            return True
        if(x==0):
            return False

count = 0

n = int(input())

for i in range(1,n+1):
    if gcd(i,n):
        count+=1

print(count)