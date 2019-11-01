#include <iostream>

using namespace std;

int main(void)
{
    int N=0;
    cin >> N;
    long int number=0, total=0;
    for(int i = 0 ; i < N ; i++){
        cin >> number;
        total += number;
    }

    cout << total << endl;
}
