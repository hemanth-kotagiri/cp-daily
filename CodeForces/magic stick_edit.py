testCases = int(input())
q = 0
answers = []
cache = {}
while q<testCases:
    number,target = input().split()
    number,target = int(number),int(target)
    if number==target or number>target:
        answers.append("YES")
        q+=1
        continue
    else:
        temp = []
        while True:
            if (number==target or number>target) and number%1==0:
                answers.append("YES")
                break
            if number>=1:
                if (number%2==0 and number<target) or number==1:
                    number = (number*3)/2
                    if number not in temp:
                        temp.append(number)
                    else:
                        answers.append("NO")
                        break
                else:
                    number-=1
                    temp.append(number)
            if number%1!=0:
                answers.append("NO")
                break
    q+=1

for answer in answers:
    print(answer)

