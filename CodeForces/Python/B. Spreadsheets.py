#This is for first type. Reverse engineer this and then second type is done!

def counter(x,count=0):
    if(x%26==0):
        return (x//26)-1,26
    return x//26,x%26
t = int(input())
answers = []

q=0

while q<t:
    test = input().upper()
    #This is for given R and C
    if(ord(test[1])<ord("A") and test.count("R")==1 and test.count("C")==1):
        number = int(test[test.index("C")+1:])
        ans = test[1:test.index("C")]
        if number<=26:
            ans = chr(64+number)+ans
        else:
            temp = ""
            while True:
                count,x = counter(number)
                if count<=26 and x<=26:
                    temp = chr(64+count)+chr(64+x)+temp
                    break
                elif count>26 and x<=26:
                    temp = chr(64+x)+temp
                    number = count
                elif count<=26 and x>26:
                    temp+=chr(count)
                    number = x
                    # counter(x)
            ans = temp+ans
        answers.append(ans)
        q+=1
    else:
        #This is for given alphabetical
        i = -1
        output = ""
        while i<len(test):
            if ord(test[i])<65:
                output=test[i]+output
                i-=1
            else:
                output = "R"+output
                break
        length = len(test)
        const = ord("A")-1
        temp = 0
        another = 0
        while i>=length*-1:
            now = test[i]
            temp += (ord(now)-const)*(26**(another))
            another +=1
            i-=1
        output = output+"C"+str(temp)
        answers.append(output)
        q+=1

for answer in answers:
    print(answer)