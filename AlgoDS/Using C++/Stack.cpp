#include <iostream>
#define MAX_SIZE 101

using namespace std;

int A[MAX_SIZE];
int top = -1;

void push(int value)
{
    if (top == MAX_SIZE -1){
        cout << "Array is full\n";
        return;
    }

    A[++top] = value;
}

void pop()
{
    if (top == -1){
        cout << "Array is empty\n";
        return;
    }

    top--;
}

int peektop()
{
    return A[top];
}

int main(void)
{
    push(1);
    push(2);
    pop();
    push(100);
    push(1000);
    pop();

    for(int i = 0 ; i <= top ; i++){
        cout << A[i] << " ";
    }
}
