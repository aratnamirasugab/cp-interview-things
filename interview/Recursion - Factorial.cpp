#include <iostream>

using namespace std;

int fac(int n)
{
    //base condition
    if (n <= 1){
        return 1;
    }else{
        return n*fac(n-1);
    }
}

int main(void)
{
    int n;
    cin >> n;

    int res = fac(n);
    cout << "Factorial of " << n << " is " << res;
}
