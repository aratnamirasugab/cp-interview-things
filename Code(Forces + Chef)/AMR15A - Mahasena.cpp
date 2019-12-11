//https://www.codechef.com/problems/AMR15A

#include <iostream>

using namespace std;

int main(void)
{
    int N;
    cin >> N;

    int A = 0;
    int even = 0, odd = 0;

    for(int i = 0 ; i < N; i++){
        cin >> A;
        if(A % 2 == 0) even++;
        else odd++;
    }

    if(even > odd)cout << "READY FOR BATTLE\n";
    else cout << "NOT READY\n";
}
