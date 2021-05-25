# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        # if node is null then return None
        if node == None:
            return None
        # if node is only one then return only head
        if node.next == None:
            return node

        currList = node
        nextList = node.next
        while(nextList):
            if nextList.val <= currList.val:
                currList.next = None
                nextList = nextList.next
            elif nextList.val > currList.val:
                currList.next = nextList
                currList.next.next = None
                
                nextList = nextList.next
        
        return currList

        # 2 -> 3 -> 1 -> 1 -> 2 -> 1 -> 4
        # 4 -> 3 -> 2 -> 1