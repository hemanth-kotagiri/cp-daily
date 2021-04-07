# Given an array, east to west.
def sol():
    arr = list(map(int, input().split()))
    # traverse from the back to start.
    prev_top = float("-inf")
    # views = []
    i = len(arr)
    count = 0
    while i > 0:
        i -= 1
        # print(arr[i], prev_top)
        if arr[i] >= prev_top:
            # views.append(arr[i])
            prev_top = arr[i]
            count += 1

    return count


print(sol())
