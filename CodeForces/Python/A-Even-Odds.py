n, k = map(int, input().split())

nums = [i for i in range(1, n+1, 2)]
for i in range(2, n+1, 2):
    nums.append(i)

print(nums[k-1])


