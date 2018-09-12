'''
problem: 1.9 - string rotation

assume you have a method 'isSubstring' which checks if a word is a substring of another.

given two strings, s1 and s2, write a function that checks if s2 is a rotation of s1 using
only one call to isSubstring

i.e. 'waterbottle' is a rotation of erbottlewat


'''

def isSubstring(string1, string2):
	return(string2 in string1)


def isRotation(str1, str2):
	newString = str2*2
	return(len(str1) == len(str2) and isSubstring(newString, str1))


def main():


	stirng1 = 'erbottlewat'
	string2 = 'waterbottle'

	if (isRotation(stirng1, string2)):
		print(stirng1, ' is a rotation of ', string2)


main()
	