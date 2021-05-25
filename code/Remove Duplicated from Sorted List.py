# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        # if head is empty -> return null
        if head == None: return None
        
        lengthList = 0
        temp = head
        while temp:
            lengthList += 1
            temp = temp.next
        
        # if length only 1 -> return head
        if lengthList == 1 : return head
        
        prev = head
        future = head.next
        while future != None:
            if future.val > prev.val:
                prev.next = future
                prev = future
            future = future.next
        prev.next = None
        
        return head

Runtime: 24 ms, faster than 94.81% of Python online submissions for Remove Duplicates from Sorted List.
Memory Usage: 13.6 MB, less than 13.55% of Python online submissions for Remove Duplicates from Sorted List.