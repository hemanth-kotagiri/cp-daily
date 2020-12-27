def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def getTwoPrimes(n):
    for i in range(2, 9990):
        if isPrime(i) and isPrime(abs(i-n)):
            print(i, abs(i-n))
            break


getTwoPrimes(16777214)

