s = input()
temp = ''
if s.count("1")<1 or s.count("0")<1 or len(s)>100:
    exit()


for i in range(len(s)):
    now = s[i]
    if temp=="":
        temp+=now
    elif now in temp:
        if len(temp)==6:
            print("YES")
            exit()
        temp+=now
    else:
        temp=""+now
print("NO")
