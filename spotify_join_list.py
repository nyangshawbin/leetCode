from calendar import c
from re import S
import sys
from collections import Counter
import heapq
# class

# Code execution starts here
if __name__=='__main__':

	initNum = [1, 4, 5, 6]
	# add 1 to the num and return [1,2,4]
	
	#combing into string, turned into int for addition
	s = [str(i) for i in initNum]
	val = int(''.join(s)) + 1

	# convert back to string, break in to digits, converted back to int
	ans = [int(a) for a in str(val)] #list comprehension	


	print(ans)

	sys.exit() #replace return in main function