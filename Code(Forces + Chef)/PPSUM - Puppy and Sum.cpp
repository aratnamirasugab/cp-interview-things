// https://www.codechef.com/problems/PPSUM

#include <iostream>

using namespace std;

int sum(int n)
{
    int temp = 0;

    while(n > 0)
    {
        temp += n;
        n--;
    }
    return temp;

}

int main(void)
{
    int res = 0, T = 0;
    cin >> T;

    while(T > 0){
        int D, N;
        cin >> D >> N;

        for(int i = 0 ; i < D ; i++){
            res = sum(N);
            N = res;
        }

        cout << res << "\n";

        T--;
    }
}
