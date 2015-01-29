import sys;

def check_fermat(a, b, c, n):
	return ["No, that doesn't work", "Holy smokes, Fermat was wrong!"][a**n + b**n == c**n and n>2];

def main(argv):
	a = int(input("First #: "))
	b = int(input("Second #: "))
	c = int(input("Third #: "))
	n = int(input("Exponent: "))
	print(check_fermat(a, b, c, n));

if __name__ == "__main__":
	main(sys.argv)