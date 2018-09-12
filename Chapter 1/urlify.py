'''
probelm 1.3 -URLify

write a method to replace all spaces in a string with '%20'. 
you may assume that the string has sufficient space at the end to hold the additional characters
'''

def urlify(someString):
	print(len(someString))
	if len(someString) <= 1:
		print('please enter a longer string')
	else:
		otherString = someString.replace(" ", "%20")
		return otherString

def main():
	print('this program takes in a string and returns its URL counterpart')
	print("\n")

	x = raw_input('enter a string: ')
	print(urlify(x))


main()