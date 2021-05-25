//https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1

Node* reverseList(Node *head)
{
  Node *first = head;
  Node *second = first->next;

  while(second != NULL){
      Node *temp = second->next;
      second->next = first;
      first = second;
      second = temp;
  }

  head->next = NULL;
  head = first;
  return head;

}
