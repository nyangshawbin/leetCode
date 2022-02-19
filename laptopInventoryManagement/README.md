## Laptop Inventory Management 

### Class LaptopInventoryManager 
```Class LaptopInventoryManager``` uses a hashtable (of fixed size k) to store all meta data about a department's laptop. <br>
The hashtable stores key-value pairs:
* Key: Generated using a hashFunction() defined as ``` key = sum(ascii values of all characters in department's name) % k```
* Value: Meta data of department, implemented using ```Class Department```. It is a linked list node. This allow us to perform chaining for collision handling of when there are conflicting hash keys.

```Class LaptopInventoryManager``` stores the spare laptop data in another data member outside the hashtable. Having this node outside the hashtable allows O(1) lookup.

Below is an illustration of the hashtable: <br>
```
{ 
 "key1": department1Node -> department2Node -> department5Node -> NULL  <br>
 "key2: department3Node -> NULL <br>
}
```

#### Methods
```python
#Returns the laptopID if successful, e.g. "A1". Returns null if no laptop is available for loan.
def borrowLaptop(self, department: str) -> str: 

#Returns the laptopID back to the inventory
def returnLaptop(self, laptopId: str) -> None:
```

### Class Department
```python
class Department:
    def __init__(self, departmentName, numOfLaptops):
        self.name = departmentName
        self.store = [1 for i in range(numOfLaptops)] # 0,1 representing absence and available of a laptop respectively
        self.numOfLaptops = numOfLaptops # number of available laptops left
        self.next = None # only used for chaining in hashtable collision handling
```
`self.store: list[int]`. Where '1' at index [i] reflects the availability of laptop#(i+1). <br> 
For eg. department 'B' has 3 laptops, laptop#2 is borrowed.
``` python
print(departmentB.name) # 'B'
print(departmentB.store) # [1, 0, 1]
print(departmentB.numOfLaptops) # 2
print(departmentB.next) # NUll
```

## Notes
Assumption made in this program:
1. All department names are in alphabets, this allow the department name and laptop IDs to be parsed when returning laptop. E.g. "ABC2", return laptopID 2 to department "ABC"
2. Departments' names are capital sensitive as the ascii values of characters are used in the hash function. 
