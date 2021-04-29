# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        print(l1)


if __name__ == '__main__':
    l1 = [2,4,3] 
    l2 = [5,6,4]
    sol = Solution().addTwoNumbers(l1,l2)
    print(sol)
        
        