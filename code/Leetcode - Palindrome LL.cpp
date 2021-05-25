//https://leetcode.com/problems/palindrome-linked-list/

//my solution works in logic
class Solution {
public:
    bool isPalindrome(ListNode* head) {

        ListNode* temp = head;
        int length = 0;
        while(temp != NULL){
            length++;
            temp = temp->next;
        }

        length = (length/2);

        if  (length % 2 == 0){
            bool res = false;
            ListNode* curr = NULL;
            ListNode* prev = NULL;
            ListNode* next = head;
            for (int i = 0 ; i < length ; i++){
                curr = next;
                curr->next = prev;
                next = next->next;
                prev = curr;
            }
            ListNode* first = curr;
            ListNode* second = next;

            while(first != NULL && second != NULL){
                if(first->val == second->val){
                    res = true;
                    first = first->next;
                    second = second->next;
                }
            }
            return res;
        }else{
            bool res = false;
            ListNode* curr = NULL;
            ListNode* prev = NULL;
            ListNode* next = head;
            ListNode* fastHead = head->next;
            for(int i = 0 ; i < length ; i++){
                curr = next;
                curr->next = prev;
                next = next->next;
                prev = curr;
                fastHead = fastHead->next;
            }
            ListNode* first = curr;
            ListNode* second = fastHead;

            while(first != NULL && second != NULL){
                if(first->val == second->val){
                    res = true;
                    first = first->next;
                    second = second->next;
                }
            }
            return res;
        }
    }
};

// O(n) time and O(1) memory
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if(head==NULL||head->next==NULL)
            return true;
        ListNode* slow=head;
        ListNode* fast=head;
        while(fast->next!=NULL&&fast->next->next!=NULL){
            slow=slow->next;
            fast=fast->next->next;
        }
        slow->next=reverseList(slow->next);
        slow=slow->next;
        while(slow!=NULL){
            if(head->val!=slow->val)
                return false;
            head=head->next;
            slow=slow->next;
        }
        return true;
    }
    ListNode* reverseList(ListNode* head) {
        ListNode* pre=NULL;
        ListNode* next=NULL;
        while(head!=NULL){
            next=head->next;
            head->next=pre;
            pre=head;
            head=next;
        }
        return pre;
    }
};

