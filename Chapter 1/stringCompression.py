'''
string compression:

implement a method to perform a basic string compression using the counts of repeated characters. 
For example, if the string is aabcccccaaa would become a2b1c5e3. 

'''

def stringCompression(someString):
	res = []
	count = 0
	prev = someString[0]

	for char in someString:
		if char == prev:
			count += 1
		else:
			res += prev + str(count)
			prev = char
			count = 1

	res += prev + str(count)
	res = ''.join(res)
	
	return (res)

	


def main():
	print('this program compresses a string using counts of repeated characters')
	print("\n")

	x = raw_input('please enter a string you would like to compress: ')

	y = stringCompression(x)

	print(x, y)

main()