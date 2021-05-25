//https://www.codechef.com/problems/PRB01
#include <iostream>

using namespace std;

int main(void)
{
    int T;
    cin >> T;

    int N = 0;

    while(T > 0)
    {
        cin >> N;

        int mid = N/2;
        bool flag = true;

        for(int i = 2 ; i <= mid ; i++){
            if(N % i == 0)flag = false;
        }

        if(flag == true){
            cout << "yes\n";
        }else{
            cout << "no\n";
        }

        T--;
    }
}
