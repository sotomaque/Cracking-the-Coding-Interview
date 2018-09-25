class Node:

	def __init__(self, data):
		self.next = None
		self.data = data

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setNext(self, newNext):
		self.next = newNext


class LinkedList:

	def __init__(self, head):
		self.head = head

	def insert(self, data):
		newNode = Node(data)
		newNode.setNext(self.head)
		self.head = newNode

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.getNext()
		return count

	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.getNext() == data:
				found = True
			else:
				current = current.getNext()
		if current is None:
			raise ValueError("Data not in list")
		return current

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.getNext() == data:
				found = True
			else:
				previous = current
				current = current.getNext()

		if current is None:
			raise ValueError('Data not in list')
		if previous is None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())



