#include <iostream>

using namespace std;

int queue[10];
int front = 0;
int rear = 0;

void Enque(int val)
{
    if (rear == 10){
        cout << "Overflow\n";
    }else{
        queue[++rear] = val;
    }
}

void Deque()
{
    if (rear = 0 && rear == front){
        cout << "Underflow\n";
    }else{
        for(int i = front ; i < rear-1 ; i++){
            queue[i] = queue[i+1];
        }
        rear = rear - 1;

    }
}

int main(void)
{
    int choose = 0;
    do{
        cout << "\n1. Enqueue\n";
        cout << "2. Dequeue\n";
        cout << "3. Print\n";
        cout << "Choose [1-3] : ";

        switch(choose)
        {
        case 1:
            break;
        case 2:
            break;
        case 3:
            break;
        }
    }while(choose != 0);
}
