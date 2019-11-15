#include <iostream>
#include <algorithm>
#include <stack>
#include <vector>
#include <queue>

using namespace std;

struct Node{
    int value;
    Node* left;
    Node* right;
};

//declare vector & stack to hold value
vector<int> vec;
stack<Node*> stek;

Node* newNode(int value)
{
    Node* temp = new Node();
    temp->value = value;
    temp->left = temp->right = NULL;
    return temp;
}

// Iterative DFS : Pre, In, Post

void In(Node* root)
{
    Node* temp = root;

    while(temp != NULL || stek.empty() == false){

        while(temp != NULL){
            stek.push(temp);
            temp = temp->left;
        }

        temp = stek.top();
        vec.push_back(temp->value);
        stek.pop();

        temp = temp->right;
    }
}

void pre(Node* root)
{
    Node* temp = root;

    while(temp != NULL || stek.empty() == false)
    {
        stek.push(temp);
        vec.push_back(temp);

        temp = temp->left;
        if(temp == NULL){
            temp = stek.top();
        }

        temp = temp->right;
    }
}

int main(void)
{
    Node* root = newNode(50);
    root->left = newNode(5);
    root->right = newNode(100);
    root->left->left = newNode(1);
    root->left->right = newNode(25);
    root->right->left = newNode(70);
    root->right->right = newNode(999);

    //select one algo :
    In(root);

    for(int i = 0 ; i < vec.size() ; i++){
        cout << vec[i] << " ";
    }
}
