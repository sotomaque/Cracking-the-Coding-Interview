'''
problem: 1.7 - matrix rotation

given an image represented by an N/N matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

'''

def rotated(array_2d):
	print('first array is reversed')
	print(array_2d[::-1])
	print("\n")
	list_of_tuples = zip(*array_2d[::-1])

	print(list_of_tuples)
	return [list(elem) for elem in list_of_tuples]

def main():
	original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(list(rotated(original)))

main()