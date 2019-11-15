#include <iostream>
#include <cstdlib>
#include <conio.h>

using namespace std;

struct node{
    int val;
    struct node* left;
    struct node* right;
};

//function to construct node
struct node* newNode(int val)
{
    struct node* temp = new node();
    temp->val = val;
    temp->left = temp->right = NULL;
    return temp;
};

//function to insert new node into list
struct node* insert(struct node* root, int val)
{
    if (root == NULL)return newNode(val);

    if (val < root->val){
        root->left = insert(root->left, val);
    }else if(val > root->val){
        root->right = insert(root->right, val);
    }

    return root;
};

//function to print tree's values inorder
void inorder(struct node* root)
{
    if (root == NULL) return;

    inorder(root->left);
    cout << root->val << " ";
    inorder(root->right);
}

//function to find the smallest number
int min(struct node* root)
{
    struct node* temp = root;

    while(temp && temp->left != NULL){
        temp = temp->left;
    }

    return temp->val;
}

int max(struct node* root)
{
    struct node* temp = root;

    while(temp && temp->right != NULL){
        temp = temp->right;
    }

    return temp->val;
}

struct node* findMin(struct node* root)
{
    struct node* temp = root;

    while(temp && temp->left != NULL){
        temp = temp->left;
    }

    return temp;
};

struct node* deleteNode(struct node* root, int val)
{
    if (root == NULL)return root;
    else if(val < root->val){
        root->left = deleteNode(root->left, val);
    }else if(val > root->val){
        root->right = deleteNode(root->right, val);
    }else{
        if(root->left == NULL && root->right == NULL){
            delete(root);
        }else if (root->left == NULL){
            struct node* temp = root;
            root = root->right;
            delete(temp);
        }else if (root->right == NULL){
            struct node* temp = root;
            root = root->left;
            delete(temp);
        }else{
            //if a node has 2 child, find its lowest right child
            struct node* temp = findMin(root->right);
            root->val = temp->val;
            root->right = deleteNode(root->right, temp->val);
        }
        return root;
    }

};

int main(void)
{
    int option = 0;
    int val;
    struct node* root = NULL;

    do{
        system("cls");
        inorder(root);
        cout << "\n\n1. Insert new value\n";
        cout << "2. Find min & max number\n";
        cout << "3. Delete a node\n";
        cout << "0. Exit\n";
        cout << "Choose : ";

        cin >> option;

        switch(option)
        {
        case 1:
            system("cls");
            cout << "Insert value : ";
            cin >> val;
            root = insert(root, val);
            break;
        case 2:
            system("cls");
            cout << "The smallest and the biggest value is : " << min(root) << " " << max(root);
            getch();
            break;
        case 3:
            cout << "Insert value to delete : ";
            cin >> val;
            deleteNode(root, val);
            break;
        }
    }while(option != 0);
}
