t = int(input())
answers = []
for i in range(t):
    givenAngle = int(input())
    now = 360/(180-givenAngle)
    if now==int(now):
        answers.append("YES")
    else:
        answers.append("NO")

for answer in answers:
    print(answer)
