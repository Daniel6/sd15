def foo(listy):
	return sum([sum(i) for i in listy])

print foo([[1,2,3],[1,2,3],[2,2,2]])