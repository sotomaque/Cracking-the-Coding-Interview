'''
problem 1.2 - check permutation

given two strings, write a method to decide if one is a permutation of the other.

different methods:
	-> after data checks have been done, 
	add elements from string 1 to an array or a hashmap,
	removing them from data structure as you read them from string 2
'''

def checkPermutation(string1, string2):
	#to be a permutation of eachother, both strings would have to contain the same character set

	if (len(string1) != len(string2)):
		return False

	elif string1 == string2:
		return True

	else:
		characters = []
		for i in string1:
			characters.append(str(i))

		# now characters[] should contain all char's from string 1
		# iterate thorough string2 removing elements from characters[] as you read them
		print('stirng 1 contains:', characters)

		for j in string2:
			if str(j) in characters:
				characters.remove(str(j))
			else:
				return False

		return True



def main():
	print('this program checks if two strings are permutations of each other')
	print("\n")

	x = raw_input('enter a string: ')
	y = raw_input('enter a second string: ')

	if (checkPermutation(x, y)):
		print(x, y, 'are permutations of each other')
	else:
		print(x, y, 'are not permutations of each other')


main()