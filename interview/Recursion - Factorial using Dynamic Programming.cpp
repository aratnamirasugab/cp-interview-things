#include <iostream>
using namespace std;

//set array as global
int res[1000] = {0};

int fac(int n)
{
    cout << "run\n";
    if (n >= 0){
        res[0] = 1;
        for (int i = 1 ; i <= n ; i++){
            res[i] = i * res[i-1];
        }

        return res[n];
    }
}

int main(void)
{
    int n;
    cin >> n;
    int res = fac(n);
    cout << "Factorial of " << n << " is " << res;
}
