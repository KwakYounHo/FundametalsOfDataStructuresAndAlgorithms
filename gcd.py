# This algorithm name is the Euclidean algorithm.
# My implementation of the Euclidean algorithm to find the greatest common divisor of two numbers
# def gcd(x,y):
# 	if min(x,y) != 0:
# 		if x > y:
# 			return gcd(x-y, y)
# 		else:
# 			return gcd(x, y-x)
# 	else:
# 		return max(x,y)
	
# Professors implementation
def gcd(x, y):
	while x != 0 and y != 0:
		if x > y:
			x = x-y
		else:
			y = y-x
	return x + y

print(gcd(8, 3))