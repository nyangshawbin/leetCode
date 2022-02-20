from calendar import c
from re import S
import sys

# class

# Code execution starts here
if __name__=='__main__':

	input = "This_is_a_demo_"
	caps = False
	first = True
	output=""
	for w in input:
		if w.isalnum():
			if caps:
				if first:
					w = w.lower()
					first = False
				else:
					w = w.upper()	
				
				caps = False
			else:
				w = w.lower()

			output +=w

		else:
			caps = True


	print("input: " + str(input) + ", output: " + str(output))
	print("test is: " + str(output == "thisIsADemo"))
	

	sys.exit() #replace return in main function