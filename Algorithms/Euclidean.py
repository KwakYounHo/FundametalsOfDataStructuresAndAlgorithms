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
	
# Professors implementation - gcd_sub
def gcd_subtract(x, y):
	while x != 0 and y != 0:
		if x > y:
			x = x-y
		else:
			y = y-x
	return max(x, y)

# Professors implementation - gcd_mod
def gcd_modular(x, y):
	while y != 0:
		x, y = y, x % y
	return x

# Professors implementation - gcd_rec
def gcd_recursive(x, y):
	if y == 0:
		return x
	else:
		return gcd_recursive(y, x % y)
	# return x if y == 0 else gcd_recursive(y, x % y)

print(gcd_subtract(32, 77))
print(gcd_modular(2, 100))
print(gcd_recursive(12, 48))
