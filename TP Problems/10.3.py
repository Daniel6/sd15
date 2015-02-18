def foo(lis):
	return ( [sum(lis[0:i]) for i in range(1,len(lis)+1)] )

print foo([1,2,3,4,5])