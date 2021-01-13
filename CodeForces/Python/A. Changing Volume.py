n = int (input ())
answers  =[]
for i in range (n):
  a,b = map(int,input().split(" "))
 
  temp = abs(b-a)
  total = (temp//5)
 
  rem = temp%5
 
  if rem and ((rem%2==0 and rem!=2) or rem==3):
    total += 2
  elif rem:
      total += 1
  answers.append(total)
 
for ans in answers:
  print(ans) 


    
    # temp=0
    # if a>b:
    #     temp = a-5
    #     if temp>0:
    #         count+= ceil(temp/5)
    #         print(count)
    #     if (a-temp)%5==1 or (a-temp)%5==2:
    #         count+=1
    #     elif (a-count)%5!=0:
    #         count+=2
    #     answers.append(count)
    # else:
    #     now = b-a
    #     count+=now//5
    #     temp = now%5
    #     if temp==1 or temp==2:
    #         count+=1
    #     elif temp!=0:
    #         count+=2
    #     answers.append(count)
# for answer in answers:
#     print(answer)