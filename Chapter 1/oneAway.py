'''
problem 1.5 - one away

there are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

i.e. 

pale, ple -> true
pales, pale -> true
pale, bake -> false

# ideas
1) create hashmap of strings. 
	-> check to see if they have more overlap than difference
'''

def oneEditAway(string1, string2):
	# if strings are identical -> true
	if string1 == string2:
		return True

	# if strings have a len difference greater than 1 -> false
	elif (len(string1) >= 2 + len(string2)) or (len(string2) >= 2 + len(string1)):
		return False
	
	# otherwise map both strings -> hashmaps
	else:
		first = {}
		first = addStringToHashmap(string1)

		second = {}
		second = addStringToHashmap(string2)

	# check to see if char difference count > 1
	for i in first:
		if i in second:
			#if character is in both strings, but difference in count > 1
			if ((second[i] - first[i]) > 1):
				print(i, 'count difference > 1')
				return False

			elif ((first[i] - second[i]) > 1):
				print(i, 'count difference > 1')
				return False

			else:
				continue

	# check to see if chars not found in one string do not exceed 1
	count = 0
	for i in first:
		if i not in second:
			count +=1
			if count > 1:
				return False
			elif first[i] > 1:
				return False
			else:
				continue

	count = 0
	for i in second:
		if i not in first:
			count += 1
			if count > 1:
				return False
			elif second[i] > 1:
				return False
			else:
				continue

	# check to make sure there is not more than 1 char found in a string and not in the other

	return True


def addStringToHashmap(someString):
	hashMapString = {}
	count = 0
	for i in someString:
		count = someString.count(i)
		if i in hashMapString: 
			hashMapString[i] += 1
		else:
			hashMapString[i] = 1
	return hashMapString


def main():
	print('this program checks to see if two strings are one edit away from each other')
	print("\n")
	x = raw_input('enter a string: ')
	y = raw_input('enter another string: ')

	if (oneEditAway(x, y)):
		print('True', x, y, ' are one edit away from each other')
	else:
		print('False', x, y, ' are not one edit away from each other')


main()