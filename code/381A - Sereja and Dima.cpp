#include <iostream>

using namespace std;

struct Node()
{
    int data;
    struct Node *next;
    struct Node *prev;
};

struct Node *head, *tail;

*head = NULL;
*tail = NULL;

void pushNode(int data)
{
    struct Node *temp = (struct Node*)malloc(sizeof(struct Node));
    *temp->data = data;
    *temp->next = *temp->prev = NULL;

    if (head == NULL){
        head = temp;
        tail = temp;
    }
    else{
        temp->next = head;
        head = temp;
    }
    return head;
};

int calculatePoint()
{
    if(head->data > tail->data){
        return head->data;
        head = head->next;
    }else{
        return tail->data;
        tail = tail->prev;
    }
}

int main(void)
{
    int n;
    cin >> n;

    int serejaPoint = 0, dimaPoint = 0;
    int data;

    for(int i = 0 ; i < n ; i++){
        cin >> data;
        pushNode(data);
    }

    for(int i = 1 ; i <= n ; i++){
        if (i % 2 == 0){
            serejaPoint += calculatePoint();
        }else{

        }
    }


}
