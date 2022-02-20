# Implemented by: NyangShawBin, nyangshawbin@gmail.com

import sys

class Department:
    def __init__(self, departmentName, numOfLaptops):
        self.name = departmentName
        self.store = [1 for i in range(numOfLaptops)]
        self.numOfLaptops = numOfLaptops
        self.next = None

class LaptopInventoryManager:
    def __init__(self, departmentNumLaptopsMap, numSpareLaptops):

        # dictionary to store departments' meta data (implemented by 'Department' Class above)
        self.hashtable = {}
        self.sizeHashTable = 7
        self.populateDepartmentHashTable(departmentNumLaptopsMap)
        
        # meta data of spare laptops
        self.spareDepartment = None
        self.populateSpareData(numSpareLaptops)

    # rudimentary implementation of using (sum of ascii values of all ch in department's name) % k, with k being the size of hash table
    def hashFunction(self, departmentName):
        val = sum(ord(ch) for ch in departmentName)
        key = val % self.sizeHashTable
        return key
    
    # Insert departmentData into hashtable
    def insertDepartmentData(self, departmentName, departmentData):
    
        # hashing department name 
        key = self.hashFunction(departmentName)

        # if key doesnt yet exist in hashtable, add data directly
        if self.hashtable.get(key) is None:
            self.hashtable[key] = departmentData
            #print('department name mapped to', key, 'inserted directly')

        # if key already exist, perform collision handling
        # add departmentData to start of chain (O(1) as compared to O(m), with m being the number departmentData at key)
        else:

            #let new data point to current head
            departmentData.next = self.hashtable[key]
            #replace current head in hashtable with new data
            self.hashtable[key] = departmentData

            #print('department name mapped to', key, 'data inserted by chaining')
    
    # querying department data from hashtable
    def findDepartmentData(self, departmentName):
        key = self.hashFunction(departmentName)
        curr = self.hashtable.get(key)

        while curr:
            if curr.name != departmentName and curr.next:
                print('department not found, trying next chain!')
                curr = curr.next
            else:
                print('department found!')
                print("name:", curr.name, ", qty:" , curr.numOfLaptops, ", store:", curr.store)
                return curr

        # department doesnt exist
        return None
    
    # initializing all departments data into the hashtable
    def populateDepartmentHashTable(self, departmentNumLaptopsMap):

        # for each department
        for departmentName, numLaptops in  departmentNumLaptopsMap.items():
            
            #intantiate a department object, and insert departmentData into hashtable
            departmentData = Department(departmentName, numLaptops)
            self.insertDepartmentData(departmentName, departmentData)

    # initializing spare department laptops outside the hashtable
    def populateSpareData(self, numSpareLaptops): 
        self.spareDepartment = Department('S', numSpareLaptops)

    def borrowLaptop(self, department):
        
        departmentData = self.findDepartmentData(department)

        # if department exist and data is found
        if departmentData is not None:

            # if department has laptops
            if departmentData.numOfLaptops > 0:
                print('Borrowing from department...')
                departmentData.numOfLaptops -=1

                # find ID of next available laptop (earliest '1' in list)
                id = departmentData.store.index(1)
                # flip status to '0'
                departmentData.store[id]=0
                
                return str(departmentData.name) + str(id+1)
            
            #if department ran out of laptops and company has spare
            elif self.spareDepartment.numOfLaptops > 0:
                print('Borrowing from spare...')
                self.spareDepartment.numOfLaptops -=1

                # find ID of next available laptop (earliest '1' in list)
                id = self.spareDepartment.store.index(1)
                # flip status to '0'
                self.spareDepartment.store[id] = 0
                
                return str(self.spareDepartment.name) + str(id+1)

            else:
                print('Both department and spare has no laptops...')
                return None
        else:
            print('Department not found...')
            return None

    def returnLaptop(self, laptopId):

        indexOfNumeric = None
        for i in range(len(laptopId)):
            if laptopId[i].isnumeric():
                indexOfNumeric = i
                break
        
        department = laptopId[:indexOfNumeric]
        id = int(laptopId[indexOfNumeric:])
        print("returning laptop id: ", id , " to department: ", department)

        departmentData = self.findDepartmentData(department)

        if departmentData:
            #update laptop status         
            if department == 'S': #not spare
                self.spareDepartment.numOfLaptops += 1
                self.spareDepartment.store[id-1] = 1
            else:
                departmentData.numOfLaptops +=1
                departmentData.store[id-1] =1

    # util to check if department is inserted into hashtable
    def showDepartmentLaptops(self):
        print('Hashtable for departments:')
        for key, departmentData in self.hashtable.items():
            listOfAllDepartment = ""
            while departmentData:
                listOfAllDepartment += departmentData.name + " "
                departmentData = departmentData.next
            
            print("Key:", key, "All Department:", listOfAllDepartment)
    
    # util to check spare department laptops
    def showSpareLaptops(self):
        print('Spare:')
        print(self.spareDepartment.name , self.spareDepartment.store)

if __name__=='__main__':

    numSpareLaptops = 2
    departmentLaptops = {"A": 2, "B": 1, "C": 0}
    mgr = LaptopInventoryManager( departmentLaptops, numSpareLaptops)

    #before
    print('Before:', )
    mgr.showDepartmentLaptops()
    mgr.showSpareLaptops()
    print()

    # PUZZLE DESCRIPTION
    print("assigned ID: ", mgr.borrowLaptop('A')) # A has 1 left
    print("assigned ID: ", mgr.borrowLaptop('A')) # A has 0 left
    print("assigned ID: ", mgr.borrowLaptop('B')) # B has 0 left
    print("assigned ID: ", mgr.borrowLaptop('C')) # C takes from Spare, Spare has 1 left
    print("assigned ID: ", mgr.borrowLaptop('A')) # A takes from Spare, Spare has 0 left
    print("assigned ID: ", mgr.borrowLaptop('B')) # No laptops available for loan
    mgr.returnLaptop("A1") # A has 1 left
    print("assigned ID: ", mgr.borrowLaptop('B')) # No laptops available for loan
    mgr.returnLaptop("S1") # Spare has 1 left
    print("assigned ID: ", mgr.borrowLaptop('B')) # B takes from Spare, Spare has 0 left


    sys.exit() #replace return in main function

