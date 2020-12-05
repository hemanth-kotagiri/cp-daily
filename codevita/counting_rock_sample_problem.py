S, R = map(int, input().split())
sizes = list(map(int, input().split()))
ranges = [list(map(int, input().split())) for _ in range(R)]
accepts = [0 for _ in range(len(ranges))]

for size in sizes:
    for i in range(len(ranges)):
        if ranges[i][0] < size < ranges[i][1]:
            accepts[i] = accepts[i] + 1

for accept in accepts:
    print(accept)
