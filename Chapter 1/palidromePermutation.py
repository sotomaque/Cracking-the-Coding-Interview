'''
problem 1.4 - palidrome permutation

given a string, write a function to check if it is a permutation of a palidrome. a palidrome is a word or phrase that is the same forwards and backwards. a permutation is a rearrangement of letters. the palidrome does not need to be limited to just dictionary words.

ideas:

- create a hashmap, {key: value} -> {letter: count}
- for string to be a palidrome (or permutation of one):
	- in the case the length of the string is even:
		- every character should have a count of 2 (or that is a multiple of 2)
	- in the case the length of the string is odd:
		- every character - 1 should have a count of 2 (or a multiple of 2)
		- while one character (the middle one) has a count of 1 (or an add # > 1)

'''

def palidromePermutation(someString):

	#convert string into hashmap
	chars = {}
	count = 0
	for i in someString:
		count = someString.count(i)
		if i in chars: 
			chars[i] += 1
		else:
			chars[i] = 1

	#check hashmap for conditions needed to be permuted into a palidrome
	if len(someString) % 2 == 0:
		#ensure count of all elements in hashmap is even
		for i in chars:
			if chars[i] % 2 != 0:
				return False
		return True
	else:
		#ensure count of all elements in hashmap is odd
		temp = 0 
		for i in chars:
			if chars[i] % 2 != 0:
				temp += 1
				if temp > 1:
					return False
		return True

	


def main():
	print('this program checks if a string can be reordered into a palidrome')
	print("\n")
	x = raw_input('enter a string: ')
	y = x.replace(" ", "")
	if (palidromePermutation(y)):
		print(x, ' is a permutation of a palidrome')
	else:
		print(x, 'is not a permutation of a palidrome')


main()

