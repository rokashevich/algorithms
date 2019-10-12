import sys
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib(n-1)+fib(n-2)

if len(sys.argv) != 2:
	print("Usage: %s n"%sys.argv[0])
else:
	nth = fib(int(sys.argv[1]))
	print(nth)