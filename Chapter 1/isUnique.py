'''
Problem 1.1 - is Unique

Implement an algorithm to determine if a string has all unique characters.
use no extra data structures (i.e. no hashmaps)
'''

def isUnique(someString):
	
	if len(someString) < 1:
		print('invalid data entry')
		return False

	elif (len(someString) == 1):
		return True

	else:
		total = 0
		
		for i in someString:
			count = someString.count(i)
			if count > 1:
				total += count

		if total > 0:
			print("duplicates were found")
			return False
		else:
			print("no duplicates found")
			return True


def main():
	#description
	print('this program checks if a string contains duplicate elements')
	print("\n")
	#get input
	x = raw_input('enter a string: ')

	isUnique(x)

main()