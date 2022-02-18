import sys


# Assumption:
# 1. all department names are strings 



# class
class LaptopInventoryManager:

    def __init__(self, departmentNumLaptopsMap, numSpareLaptops):

        # dictionary to store departments' laptops meta data 
        # meta data: [ No. of laptops department has, [status of each laptop]] . Borrowed laptops are absent from store, hence denoated as '0'
        # E.g. Depart A has 2 laptops, none borrowed
        # E.g. Depart B has 3 laptops, #2 laptop borrowed
        # E.g. Depart C has 0 laptops
        # E.g. departmentLaptops = {'A': [2, [1, 1]], 'B': [3, [1, 0, 1]], 'C': [0, []] }
        self.departmentLaptops = {}

        # 3 spare laptops in company
        # E.g. SpareLaptops = {'S': [3, [1, 1, 1]] }
        self.spareLaptops = {}
        self.spareLaptopPrefix = 'S'

        self.sizeHashTable = 100
        self.initDepartmentData(departmentNumLaptopsMap)
        self.initSpareData(numSpareLaptops)


    # populate meta data for each department
    def initDepartmentData(self, departmentNumLaptopsMap):
        
        for departmentName, numLaptops in  departmentNumLaptopsMap.items():
            metaData = []
            metaData.append(numLaptops)
            metaData.append([1 for i in range(numLaptops)])
            self.departmentLaptops[departmentName] = metaData

    # populate meta data for spare
    def initSpareData(self, numSpareLaptops):
        metaData = []
        metaData.append(numSpareLaptops)
        metaData.append([1 for i in range(numSpareLaptops)])
        self.spareLaptops[self.spareLaptopPrefix] = metaData

    def borrowLaptop(self, department):
        
        id = None
        departmentName =department

        #if department has laptops
        if self.departmentLaptops[department][0] > 0:
            self.departmentLaptops[department][0] -=1

            # find ID of next available laptop (earliest '1' in list)
            id = self.departmentLaptops[department][1].index(1)
            # change status to '0'
            self.departmentLaptops[department][1][id]=0
            
            return str(departmentName) + str(id+1)
        
        #if department ran out of laptops, company has spare
        elif self.spareLaptops[self.spareLaptopPrefix][0] > 0:
            self.spareLaptops[self.spareLaptopPrefix][0] -=1

            # find ID of next available laptop (earliest '1' in list)
            id = self.spareLaptops[self.spareLaptopPrefix][1].index(1) 

            # change status to '0'
            self.spareLaptops[self.spareLaptopPrefix][1][id]=0
            
            return str(self.spareLaptopPrefix) + str(id+1)

        else:
            return None

    def returnLaptop(self, laptopId):
        department = ""
        id = indexOfNumeric = None
    
        for i in range(len(laptopId)):
            if laptopId[i].isnumeric():
                indexOfNumeric = i
                break
        department = laptopId[:indexOfNumeric]
        id = int(laptopId[indexOfNumeric:])
        
        print("returned laptop id: ", id , " to department: ", department)
        
        if department != 'S':
            #update the returned laptop in respective store
            self.departmentLaptops[department][0] +=1
            #change status of laptop
            self.departmentLaptops[department][1][id-1] =1
        else:
            #update the returned laptop in respective store
            self.spareLaptops[department][0] +=1
            #change status of laptop
            self.spareLaptops[department][1][id-1] =1

    def hashFunction(self, departmentName):
        
        val = sum(ord(ch) for ch in departmentName)
        key = val % self.sizeHashTable


    
    def showDepartmentLaptops(self):
        print(self.departmentLaptops)
    
    def showSpareLaptops(self):
        print(self.spareLaptops)

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
    print(mgr.borrowLaptop('A')) # A has 1 left
    print(mgr.borrowLaptop('A')) # A has 0 left
    print(mgr.borrowLaptop('B')) # B has 0 left
    print(mgr.borrowLaptop('C')) # C takes from Spare, Spare has 1 left
    print(mgr.borrowLaptop('A')) # A takes from Spare, Spare has 0 left
    print(mgr.borrowLaptop('B')) # No laptops available for loan
    mgr.returnLaptop("A1") # A has 1 left
    print(mgr.borrowLaptop('B')) # No laptops available for loan
    mgr.returnLaptop("S1") # Spare has 1 left
    print(mgr.borrowLaptop('B')) # B takes from Spare, Spare has 0 left

    #after
    print()
    print('After:', )
    mgr.showDepartmentLaptops()
    mgr.showSpareLaptops()


	#call whichever function

    sys.exit() #replace return in main function

