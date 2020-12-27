def minimumDistances(givenList,cp,k):
    # givenList.sort(key = lambda k: (k[0]-cp[0])**2+(k[1]-cp[1])**2)
    # return givenList[:k]
    temp = k
    minDistances = {}
    for index in range(len(givenList)):
        point = givenList[index]
        distance = (point[1]-cp[1])**2+(point[0]-cp[0])**2
        if temp>0:
            minDistances[distance] = list(point)
            temp-=1
        else:
            maxPointDistance = max(minDistances.keys())
            if maxPointDistance > distance:
                del minDistances[maxPointDistance]
                if distance in minDistances.keys():
                    minDistances[distance].append(point)
                else:
                    minDistances[distance] = point

    mins = minDistances.values()
    return list(mins)

pointsList =  [[0,1],[1,0]]
cp = (0,0)
k = 2

print(minimumDistances(pointsList,cp,k))