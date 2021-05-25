//https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/

Runtime: 0 ms, faster than 100.00% of C++ online submissions for Binary Tree Inorder Traversal.
Memory Usage: 9.3 MB, less than 84.00% of C++ online submissions for Binary Tree Inorder Traversal.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

//iteratively
#include <stack>
#include <vector>

class Solution {
public:

  stack<TreeNode*>st;
    vector<int>vec;

    vector<int> inorderTraversal(TreeNode* root) {
        inorderIterative(root);
        return vec;
    }

    void inorderIterative(TreeNode* root)
    {
        TreeNode* curr = root;
        while(curr != NULL || st.empty() == false){

            while(curr != NULL){
                st.push(curr);
                curr = curr->left;
            }

            curr = st.top();
            st.pop();

            vec.push_back(curr->val);

            curr = curr->right;
        }
    }
};

// using recursive

#include <vector>
class Solution {
public:

    vector<int> vec;

    vector<int> inorderTraversal(TreeNode* root) {
        inorder(root);
        return vec;
    }

    void inorder(TreeNode* root){

        if(root == NULL){
            return;
        }

        inorder(root->left);
        vec.push_back(root->val);
        inorder(root->right);
    }
};
