n = int(input())
numbers = [int(i) for i in input().split(" ")]
i=0
while len(numbers)!=1:
    numbers.remove(max(numbers))
    if len(numbers)==1:
        print(numbers[0])
        exit()
    numbers.remove(min(numbers))
print(numbers[0])