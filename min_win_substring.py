# class
from collections import Counter
import sys


# Code execution starts here
if __name__=='__main__':

    s = "ADOBECODEBANC"
    t = "ABC"
    
    # s='a'
    # t='aa'
    if not s or not t or len(s) < len(t):
        print('')
        sys.exit()
    
    t_counter = Counter(t)
    chars = len(t_counter.keys()) #unique chars in t
        
    s_counter = Counter()
    matches = 0
    
    answer = ''
    
    i = 0
    j = -1 # make j = -1 to start, so we can move it forward and put s[0] in s_counter in the extend phase 
    
    #iterate through each char in s
    while i < len(s):
        
        # extend
        if matches < chars: #using unique char in t as condition
            
            # since we don't have enough matches and j is at the end of the string, we have no way to increase matches
            if j == len(s) - 1: #terminate at index 12
                print(answer)
                sys.exit()
            
            j += 1 #move back of window backwards
            s_counter[s[j]] += 1 #updating count in s_counter
            if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]: 
                matches += 1 #num of char with *matching counts*!

        # contract
        else:
            s_counter[s[i]] -= 1 #decrease count of first element in window
            if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                matches -= 1 #num of char with matching counts
            i += 1 #move front of window backward
            
        # update answer
        if matches == chars:
            if not answer: #if ans is empty
                answer = s[i:j+1]
            elif (j - i + 1) < len(answer):
                answer = s[i:j+1]
    
    print(answer)