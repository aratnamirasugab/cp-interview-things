#include <iostream>

using namespace std;

class Node{
public :
    int data;
    Node *next;
};

void printList(Node *head)
{
    while(head != NULL){
        cout << head->data << "\n";
        head = head->next;
    }
}

int main(void)
{
    Node *head = NULL;
    Node *second = NULL;

    head = new Node();
    second = new Node();

    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = NULL;

    printList(head);
}
