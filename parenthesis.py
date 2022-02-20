
def main():

    s = "([)]"
    bracketDict = {"round":0, "square":0, "curly":0}
    print(bracketDict)
    for bracket in s:
        
        # round bracket
        if bracket == "(":
            
            bracketDict["round"] +=1
            
        if bracket == ")":
            if bracketDict["round"] ==0:
                return False
            else:
                bracketDict["round"] -=1
                
        # sqaure bracket
        if bracket == "[":
            bracketDict["square"] +=1
            
        if bracket == "]":
            if bracketDict["square"] ==0:
                return False
            else:
                bracketDict["square"] -=1
                
        # curly bracket
        if bracket == "{":
            bracketDict["curly"] +=1
            
        if bracket == "}":
            if bracketDict["curly"] ==0:
                return False
            else:
                bracketDict["curly"] -=1
                
    for value in bracketDict.values():
        if value != 0:
            return False
        
    return True

    

print(main())