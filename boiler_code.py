from re import A
import sys
from collections import deque
# class
class Node:

	def __init__(self, departmentName, numOfLaptops):
		self.name = departmentName
		self.store = [1 for i in range(numOfLaptops)]
		self.numOfLaptops = numOfLaptops
		self.next = None
		
	def initVal(self, val):
		self.value = val

# Code execution starts here
if __name__=='__main__':

	table = {}
	nodeA  = Node('A', 99)
	table["key"] = nodeA

	#attempt insert
	nodeB = Node('B', 20)
	nodeB.next = nodeA
	table["key"] = nodeB

	print(table["key"].next.name)

	sys.exit() #replace return in main function

