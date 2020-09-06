# implementation of stack
class Stack():

	# Creating an empty Stack
	def __init__(self):
		self.items = []

	#Adding an element into Stack 
	def push(self, item):
		return self.items.append(item)

	#Printing stack 
	def stack_print(self):
		return print(self.items)

	#Removing element in a Stack (LIFO) 
	def pop(self):
		last_ele = self.items[-1]
		return self.items.remove(last_ele)	

	#Checking Stack is empty or not
	def is_empty(self):
		if self.items == []:
			return print(True)
		else:
			return print(False)	


# Creating object
s = Stack()

s.is_empty()
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
s.stack_print()
s.pop()
s.stack_print()
s.is_empty()

# Output:
# True
# ['A', 'B', 'C', 'D', 'E']
# ['A', 'B', 'C', 'D']
# False



