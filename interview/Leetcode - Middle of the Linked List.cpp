//https://leetcode.com/problems/middle-of-the-linked-list/
//Runtime: 0 ms, faster than 100.00% of C++ online submissions for Middle of the Linked List.

class Solution {
public:
    ListNode* middleNode(ListNode* head) {

        ListNode* temp = head;
        int length = 0;
        while(temp != NULL){
            length++;
            temp = temp->next;
        }

        length = (length/2)+1;
        temp = head;
        for (int i = 1 ; i < length ; i++){
            temp = temp->next;
        }

        return temp;
    }
};
