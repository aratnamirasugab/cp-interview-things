//https://www.codechef.com/problems/CHOPRT
#include <iostream>

using namespace std;

int main(void)
{
    int T;
    cin >> T;

    int A,B;
    while(T > 0){
        cin >> A >> B;
        if(A > B){
            cout << ">";
        }else if(A < B){
            cout << "<";
        }else{
            cout << "=";
        }
        cout << "\n";
        T--;
    }
}
