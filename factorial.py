x = int(input('Give a number to print factorial: '))
fact = 1
for i in range(1, x+1):
	fact*=i
print(fact)