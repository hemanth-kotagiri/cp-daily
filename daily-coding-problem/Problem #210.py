import functools

# Collatz conj.

def collatz(n):
    if n == 1:
        return True
    elif n % 2 == 0:
        return collatz(n // 2)
    else:
        return collatz(3 * n + 1)

#print(collatz(20) == collatz(123103319) == collatz(123103213349))

def collatz_seq(n):
    if n == 1:
        print(1)
    elif n % 2 == 0:
        print(n)
        return collatz_seq(n // 2)
    else:
        print(n)
        return collatz_seq(3 * n + 1)


#@functools.lru_cache(maxsize = 50000000000)
def collatz_counter(n,count = 0):
    if n == 1:
        count += 1
        return count
    elif n % 2 == 0:
        count += 1
        return collatz_counter(n // 2, count)
    else:
        count += 1
        return collatz_counter(3 * n + 1, count)

tempI = 0
count = 0

for i in range(1,1000000):
    temp = collatz_counter(i)
    if count < temp:
        print(temp,tempI)
        count = temp
        tempI = i

print(tempI,count)
