//https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1

Node* rotate(Node* head, int k) {
    //this solution gave me Segmentation fault but its correct in logic
    int length = 1;
    Node *n = head;
    while(n->next != NULL)
    {
        length++;
        n = n->next;
    }

    if (k > length){
        return head;
    }else{
        Node *temp = head;
        while(k > 1)
        {
            temp = temp->next;
            k--;
        }
        Node *newHead = temp->next;
        Node *temp2 = temp->next;
        temp->next = NULL;

        while(temp2->next != NULL)
        {
            temp2 = temp2->next;
        }

        temp2->next = head;
        head = newHead;
        return head;
    }
}

// another solution O(n^2)
Node* rotate(Node* head, int k)
{
    for(int i=1;i<=k;i++)
    {
        Node *temp=head,*curr;
        head=head->next;
        curr=head;
        while(curr->next!=NULL)
        {
            curr=curr->next;
        }
        curr->next=temp;
        temp->next=NULL;

    }
    return head;
}
