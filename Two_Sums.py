# #brute force method. time complexity is O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         ans = []
        
#         n = len(nums)
#         for x in range(n-1):
#             for y in range (x+1, n): #excluding n
#                 if (nums[x]+nums[y] == target):
#                     ans.append(x);
#                     ans.append(y);
        
#         return ans

#using hashmap. time/space complexity: O(n)
#To implement this algorithm you need to iterate through each element in the given array starting from the first element. In each iteration check if required number (required  number = target sum - current number) is present in the given array. If present, return the required number, current number indexes as  result. Otherwise add the current number as key and current number index as value to the hashmap. Repeat this  until you find the result.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #dictionary
        for i, value in enumerate(nums):
            
            remaining = target - nums[i]
           
            if remaining in seen:
                return [i, seen[remaining]] # seen[remaining] returns the value (which is the index)
            
            seen[value] = i 
