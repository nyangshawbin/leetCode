import sys

# following is an illustration of using a hashtable to store our departments' data
# Departments with the same hashed keys are chain together using linkedList, implemented using the 'Department' class.
# size of hashtable is hard coded to be of length 7
# {
#  "key1": department1Data -> department2Data -> department5Data -> NULL 
#
#  "key2: department3Data -> NULL
# }


# Assumption:
# 1. all department names are alphabets, this allow the department name and laptop IDs to be parsed when returning laptop.  


# meta data of a department, implemented as a linked list. 
# # E.g. Depart A has 2 laptops, none borrowed
#       name = 'A'
#       store = [1,1]
#       numOfLaptops = 2
# E.g. Depart B has 3 laptops, laptopID:#2 laptop borrowed
#       name = 'B'
#       store = [1,0,1]
#       numOfLaptops = 3
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

    def hashFunction(self, departmentName):
        val = sum(ord(ch) for ch in departmentName)
        key = val % self.sizeHashTable
        return key
    
    # Add department data into hash table
    # perform collisin checking if key already exist
    def insertDepartmentData(self, departmentName, departmentData):
    
        # hashing department name 
        key = self.hashFunction(departmentName)

        # if key is new 
        if self.hashtable.get(key) is None:
            self.hashtable[key] = departmentData
            #print('department name mapped to', key, 'inserted directly')

        # if key in collision, perform collision handling
        # add departmentData to end of chain
        else:
            curr = self.hashtable.get(key)
            while curr.next:
                curr = curr.next
            curr.next = departmentData
            #print('department name mapped to', key, 'data inserted by chaining')
    
    def findDepartmentData(self, departmentName):
        # hashing department name 
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


    def populateDepartmentHashTable(self, departmentNumLaptopsMap):

        # for each department
        for departmentName, numLaptops in  departmentNumLaptopsMap.items():
            
            #insert department data into hashtable
            departmentData = Department(departmentName, numLaptops)
            self.insertDepartmentData(departmentName, departmentData)

    # populate meta data for spare
    def populateSpareData(self, numSpareLaptops): 
        self.spareDepartment = Department('S', numSpareLaptops)

    def borrowLaptop(self, department):
        
        id = None

        departmentData = self.findDepartmentData(department)

        if departmentData is not None:
            if departmentData.numOfLaptops > 0:
                print('Borrowing from department...')
                departmentData.numOfLaptops -=1

                # find ID of next available laptop (earliest '1' in list)
                id = departmentData.store.index(1)
                # change status to '0'
                departmentData.store[id]=0
                
                return str(departmentData.name) + str(id+1)
            
            #if department ran out of laptops, company has spare
            elif self.spareDepartment.numOfLaptops > 0:
                print('Borrowing from spare...')
                self.spareDepartment.numOfLaptops -=1

                # find ID of next available laptop (earliest '1' in list)
                id = self.spareDepartment.store.index(1)
                # change status to '0'
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
        print("returned laptop id: ", id , " to department: ", department)

        departmentData = self.findDepartmentData(department)

        #update laptop status         
        if department == 'S': #not spare
            self.spareDepartment.numOfLaptops += 1
            self.spareDepartment.store[id-1] = 1
        else:
            departmentData.numOfLaptops +=1
            departmentData.store[id-1] =1

    
    def showDepartmentLaptops(self):
        print('Hashtable for departments:')
        for key, departmentData in self.hashtable.items():
            allDepartmentInAtKey = ""
            while departmentData:
                allDepartmentInAtKey += departmentData.name + " "
                departmentData = departmentData.next
            
            print("Key:", key, "All Department:", allDepartmentInAtKey)
    
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

    #main function
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

