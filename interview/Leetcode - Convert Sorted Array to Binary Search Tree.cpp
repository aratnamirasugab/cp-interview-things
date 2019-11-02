//https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:

    TreeNode* insert(struct TreeNode* head, int val){
        TreeNode* temp = new TreeNode(val);

        if(head == NULL){
            head = temp;
        }else if(head->val < val){
            head->right = insert(head->right, val);
        }else{
            head->left = insert(head->left, val);
        }

        return head;
    }

    TreeNode* sortedArrayToBST(vector<int>& nums) {
        struct TreeNode* head = NULL;

        for(int i = 0 ; i < nums.size() ; i++){
            head = insert(head, nums[i]);
        }
        return head;
    }


};
