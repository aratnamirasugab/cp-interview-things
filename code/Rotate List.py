# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None : return head
        if head.next is None : return head
        
        lengthNode = 1
        temp = head
        while temp.next != None:
            lengthNode += 1
            temp = temp.next
        temp.next = head
    
        k = k % lengthNode
        if k == lengthNode: return head
        
        i = 0
        tempNode = head
        while i < lengthNode-k-1:
            tempNode = tempNode.next
            i += 1
            
        answer = tempNode.next
        tempNode.next = None
        
        return answer

Runtime: 32 ms, faster than 90.25% of Python3 online submissions for Rotate List.
Memory Usage: 14.3 MB, less than 30.65% of Python3 online submissions for Rotate List.
