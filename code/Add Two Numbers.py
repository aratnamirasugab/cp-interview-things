# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def iterateAndAppend(self, nodeToIterate: ListNode) -> List[int]:
        node = nodeToIterate
        res = []
        
        while node is not None:
            res.append(node.val)
            node = node.next

        res = self.reverseAndConvertToInteger(res)
        return res
    
    def reverseAndConvertToInteger(self, res: List) -> int:
        res.reverse()
        convertResToString = [str(x) for x in res]
        resString = "".join(convertResToString)
        res = int(resString)
        return res
    
    def convertDigitToListIntegerAndReverse(self, digit: int) -> List[int]:
        res = [int(x) for x in str(digit)]
        res.reverse()
        return res
    
    def appendList(self, listDigit: List[int]) -> ListNode:
        
        nodeResult = None
        head = nodeResult
        
        for x in listDigit:
            
            new_node = ListNode(x)
            
            if nodeResult == None:
                nodeResult = new_node
                head = nodeResult
            else:
                head.next = new_node
                head = head.next
        
        return nodeResult
            
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        valuel1 = self.iterateAndAppend(l1)
        valuel2 = self.iterateAndAppend(l2)
        
        res = valuel1 + valuel2
        llist = self.convertDigitToListIntegerAndReverse(res)
        nodeResult = self.appendList(llist)
        
        return nodeResult
        
# Runtime: 76 ms, faster than 22.87% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.4 MB, less than 11.80% of Python3 online submissions for Add Two Numbers.

        
    
        
        
        