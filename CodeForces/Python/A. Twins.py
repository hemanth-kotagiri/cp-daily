noOfCoins = int(input())
coins = [int(i) for i in input().split()]

#this is for 2 coins
# if len(coins)==2 and max(coins)==min(coins):
#     print(2)
#     exit()
# elif len(coins)==2:
#     print(1)
#     exit()


#This is for coins more than 2
total = 0
count = 0

while True:
    now = max(coins)
    nowIndex = coins.index(now)
    total+=now
    coins.remove(now)
    if total>sum(coins):
        count+=1
        print(count)
        exit()
    else:
        count+=1








# for i in range(len(coins)):
#     if i==0:
#         total+=coins[i]
#         count+=1
#         if total>=sum(coins[i+1:len(coins)]):
#             print(count)
#             exit()
#     else:
#         total += coins[i]
#         count+=1
#         if total>=sum(coins[i+1:len(coins)]):
#             print(count)
#             exit()
