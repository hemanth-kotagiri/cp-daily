m,s=input().split(" ")
m,s=int(m),int(s)
toLoop = int("1"+"0"*m)

for i in range(toLoop,int(str(toLoop)+"0")):
    now = str(i)
    temp = 0
    for each in now:
        temp+=int(each)
        
