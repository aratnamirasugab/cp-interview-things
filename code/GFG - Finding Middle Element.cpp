//https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

int getMiddle(Node *head)
{
    if (head == NULL){
        return -1;
    }

    int length = 0;
    Node *temp = head;
    while(temp != NULL){
        length++;
        temp = temp->next;
    }

    length = (length/2)+1;
    Node *curr = head;
    for(int i = 1 ; i < length ; i++){
        curr = curr->next;
    }

    return curr->data;

}
