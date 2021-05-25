# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        if node.next == None and node.val != target:
            return node

        if node.next == None and node.val == target:
            return None

        prevNode = None
        currNode = node
        realNode = None
        while(currNode):
            if currNode.val != target:
                realNode = currNode
            

            currNode = currNode.next




        target 1
        0 -> 1 -> 1 -> 2 -> 3 -> 1
        1 -> 2 -> 1 -> 2 -> 2


        0 -> 2 -> 3