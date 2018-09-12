'''
problem: 1.8 - Zero Matrix

write an algorithm so that, if any element in an M*N maxtrix is a zero, the entire row is zero

i.e. [[1,2,3], [4, 7, 0]]

	1    2    3			->		1 	2	3
	4    7    0					0	0	0

'''
def zeroMatrix(someArray):
	for m in range(0, len(someArray)): 		# m -> 3
		for n in range (0, len(someArray[m])):	# n -> 3
			if someArray[m][n] == 0:
				someArray[m] = zeroArray(someArray[m])
	return someArray


def zeroArray(someArray):
	for elem in range(0, len(someArray)):
		someArray[elem] = 0
	return someArray


def main():
	test = [[1,2,3], [4,7,9]]
	result = [[]]
	result = zeroMatrix(test)

	print(result)

main()