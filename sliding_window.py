import sys

# class

# Code execution starts here
if __name__=='__main__':

		
	array = [ 1,2,3,4,5,6]
	k = 3 
	
	#first sum of k elements
	window_sum = window_max = sum(array[:k])
	
	#sliding window
	for i in range(len(array)-k):
		window_sum = window_sum - array[i] + array[i+k]
		window_max = max(window_max, window_sum)
	
	
	print(window_max)


	sys.exit() #replace return in main function

