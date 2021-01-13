def almost_lucky(num):
    if not num:
        return False
    if (num % 4 == 0) or (num % 7 == 0):
        return True
    if all((x == '4' or x == '7') for x in str(num)): return True
    for i in range(4,num):
        #print(all(x == '4' or x == '7' for x in str(i)))
        #print(i)
        if all((x == '4' or x == '7') for x in str(i)):
            if num%i==0:
                return True
    return False


x = int(input())
if almost_lucky(x): print("YES")
else: print("NO")
