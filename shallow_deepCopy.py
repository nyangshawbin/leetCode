import sys

# class

# Code execution starts here
if __name__=='__main__':

	

	col = 2
	rows = 4
	#shallow list
	list = [[0] * col] * rows
	# hence all first element in each row gets manipulated
	list [2][0] = 9
	print(list[1] is list[2])
	print(list)
	


	#deep copy
	list2 = [[0 for i in range(col)] for j in range(rows)]
	list2 [2][0] = 9
	print(list2[1] is list2[2])
	print(list2)
	sys.exit() #replace return in main function

