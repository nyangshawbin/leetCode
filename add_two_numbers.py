# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        currTenthDigit = 0
        prevTenthDigit = 0
        hasTenth = False
        head = temp = ListNode()
        
        while l1 or l2: 
            nodesVal = 0
            
            if l1 and l2:
                print('both')
                print(l1.val, '+', l2.val)
                nodesVal = l1.val + l2.val
            elif l1 and not l2:
                print('either')
                nodesVal = l1.val
            elif l2 and not l1:
                print('either')
                nodesVal = l2.val
                
            sum = nodesVal + prevTenthDigit
            curr_node_val = sum % 10
            print("curr_node_val: ", curr_node_val)
            if sum>=10:
                hasTenth = True
                currTenthDigit = int(sum/10)
                print('currTenth: ', currTenthDigit)
                # update prev tenth digit
                prevTenthDigit = currTenthDigit
                
            else:
                hasTenth = False
                prevTenthDigit = 0
                
            newNode = ListNode(curr_node_val)
            temp.next = newNode
            temp = temp.next
            
          
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if hasTenth:
            print('adding last node')
            lastNode = ListNode(prevTenthDigit)
            temp.next = lastNode
        
        return head.next