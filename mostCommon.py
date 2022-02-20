import sys
from collections import Counter

# class

# Code execution starts here
if __name__=='__main__':

	testcase = [2,3,4,5,6,1,1,1,3,1,3]

	mostCommon = Counter(testcase).most_common()[:2]
	newList = [num for num, count in mostCommon]

	print(newList)
	

	sys.exit() #replace return in main function