import sys

def compare(x, y):
	if x<y:
		return -1
	elif x==y:
		return 0
	elif x>y:
		return 1

def main(argv):
	print compare(-5,-1)
	print compare(0, 2)
	print compare(-5, 12)
	print compare(12, 0)
	print compare(-1, -1)

if __name__ == "__main__":
	main(sys.argv)