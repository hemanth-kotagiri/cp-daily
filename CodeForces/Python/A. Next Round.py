#take two values sap by space call them n and k.
#n means no of participants and k is the score of kth participant to compare to all the n's

n,kthPlace = input().split(" ")
n,kthPlace = int(n),int(kthPlace)

if(1<=kthPlace<=n<=50):
    participants = [(int(i)) for i in input().split(" ")]
    compareValue = participants[kthPlace-1]
    #working for the solution
    count = 0
    for score in participants:
        if (score,compareValue)==(0,0):
            continue
        if score>=compareValue:
            count+=1

    print(count)

