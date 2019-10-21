#include <iostream>
#include <cstdlib>
#include <stdlib.h>

using namespace std;

struct Node{
    int val;
    Node *next;
};

Node *start;

void printList()
{
    Node *curr = start;
    cout << "List : ";
    while(curr != NULL)
    {
        cout << curr->val << " ";
        curr = curr->next;
    }

    cout << "\n\n\n";
}

void insertAtFront(int x)
{
    Node *curr = new Node();

    if (start == NULL){
        curr->next = NULL;
        curr->val = x;
        start = curr;
    }else{
        curr->val = x;
        curr->next = start;
        start = curr;
    }
}

int main(void)
{
    int option;
    int number;
    do{
        system("cls");
        printList();
        cout << "Insert\n";
        cout << "1. Insert at front\n";
        cout << "2. Insert at tail\n";
        cout << "Remove\n";
        cout << "3. Remove at front\n";
        cout << "4. Remove at tail\n";
        cout << "5. Search\n";
        cout << "6. Reverse\n";
        cout << "0. Exit\n";
        cout << "Choose : [1-6] : ";
        cin >> option;

        switch(option)
        {
        case 1 :
            system("cls");
            cin >> number;
            insertAtFront(number);
            break;
        case 2:
            break;
        case 3:
            break;
        case 4:
            break;
        case 5:
            break;
        case 6:
            break;
        }
    }while(option != 0);



}
