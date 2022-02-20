from calendar import c
from re import S
import sys
from collections import Counter
from abc import ABC, abstractclassmethod, abstractmethod
import heapq

# class
class car(ABC):
    def __init__(self, name):
        self.name = name
        
    def description(self):
        print("this is the parent class description. Normal~")
    
    @abstractmethod
    def price(self,x): # hide real implementation, simply an declaration. have to be implemented by child classes.
        pass


class child_car(car):
    def price(self, x):
        print(f"this {self.name} cost about {x} dollars!!!")
	


# Code execution starts here
if __name__=='__main__':

    honda = child_car("honda")
    honda.description()
    honda.price(5555)
    
    
    
    sys.exit() #replace return in main function