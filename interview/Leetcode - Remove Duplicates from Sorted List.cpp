// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

//Runtime: 12 ms, faster than 72.80% of C++ online submissions for Remove Duplicates from Sorted List.
//Memory Usage: 9.1 MB, less than 100.00% of C++ online submissions for Remove Duplicates from Sorted List.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {

        if (head == NULL || head->next == NULL){
            return head;
        }

        ListNode* curr = head;
        while (curr && curr->next) {
        if (curr->val == curr->next->val)
            curr->next = curr->next->next;
        else
            curr = curr->next;
        }
        return head;
    }
};
