def checkNonDec(array):
    i,k=0,0
    if array==sorted(array):
        return True
    for i in range(1,len(array)):
        if array[i]<array[i-1]:
            pass


print(checkNonDec([4,2,3]))
