def foo(str):
	num_a = 0
	num_b = 0
	for x in range(len(str)):
		
		if str[x]=="a" and num_a==x:
			num_a += 1
	for x in range(len(str)-1, 0, -1):
		if str[x]=="b" and num_b==len(str)-1-x:
			num_b += 1
	return num_a==num_b

print(foo("aadffdefebb"))
print(foo("abdcdsdatafsdbb"))