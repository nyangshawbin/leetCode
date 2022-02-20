import sys
# class




# Code execution starts here
if __name__=='__main__':

	p_visited = set()

	p_visited.add((2,3))
	p_visited.add((1,1))
	print(p_visited)

	directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
	for dx, dy in directions:
		print(dx, dy)
	sys.exit() #replace return in main function