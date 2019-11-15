#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

vector<int> vec;
stack<Node*> st;

struct Node{
    int value;
    Node* left;
    Node* right;
};

Node* createNode(int val)
{
    Node* temp = new Node();
    temp->value = val;
    temp->left = temp->right = NULL;
    return temp;
}

void BFSearch(Node* root)
{
    if(root == NULL) return;

    queue<Node* > q;

    q.push(root);

    while(q.empty() == false)
    {
        Node* temp = q.front();
        vec.push_back(temp->value);
        q.pop();

        if (temp->left != NULL){
            q.push(temp->left);
        }

        if (temp->right != NULL){
            q.push(temp->right);
        }
    }
}

int main(void)
{
    Node* root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);

    BFSSearch(root);

    for(int i = 0 ; i < vec.size(); i++){
        cout << vec[i] << " ";
    }
}
