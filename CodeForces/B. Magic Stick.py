t = int(input())
answers = []
i = 0
while i < t:
    number, target = input().split()
    number, target = int(number), int(target)
    if target % number == 0 and not target == number:
        answers.append("NO")
        i += 1
        continue
    if number >= target:
        answers.append("YES")
        i += 1
    else:
        temp = []
        while True:
            if number % 2 == 0:
                if number not in temp:
                    number = (number*3)/2
                    temp.append(number)
                else:
                    answers.append("NO")
                    break
            else:
                number -= 1
                if number not in temp:
                    temp.append(number)
                else:
                    answers.append("NO")
                    break
            if(number == target):
                answers.append("YES")
                break
            elif(number > target):
                if number % 1 != 0:
                    answers.append("NO")
                else:
                    answers.append("YES")
                break
        i += 1
for each in answers:
    print(each)
