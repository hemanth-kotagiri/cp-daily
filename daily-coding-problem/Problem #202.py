# Check pal without converting to string

def isPal(n):
	temp = n
	ans = 0
	while n:
		ans = ans*10 + (n%10)
		n//=10
	return temp == ans

print(isPal(132231))