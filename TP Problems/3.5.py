import sys

def drawGrid(size):
	row = "+" + size * " - - - - +"
	not_row = "|" + size * "         |"
	print row;
	for i in range(size):
		for k in range(4):
			print not_row
		print row

def main(argv):
	drawGrid(2)

if __name__ == "__main__":
	main(sys.argv);