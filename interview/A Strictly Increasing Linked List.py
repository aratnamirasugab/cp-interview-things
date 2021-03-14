# Your code took 33 milliseconds — faster than 95.30% in Python
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head):
        if head.next == None:
            return True

        prevVal = head.val
        llist = head.next
        while(llist):
            if llist.val <= prevVal:
                return False
            prevVal = llist.val
            llist = llist.next
        
        return True
            