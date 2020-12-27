def canYouReach(nums):
    startInd = 0
    while True:
        try:
            newInd = nums[startInd]
            if not newInd:
                return False
            else:
                if newInd < startInd:
                    startInd += newInd
                else:
                    startInd = newInd
        except IndexError:
            return True

arr = [1, 2, 1, 0, 0]

print(canYouReach(arr))