#include <iostream>

using namespace std;

int main(void)
{
    long long int n;
    cin >> n;
    long long int res = 0;



    if (n == 1){
        res = -1;
        cout << res << endl;
    }else if (n % 2 == 0){
        res = (n/2);
        cout << res << endl;
    }else{
        res = ((n/2) + 1) * -1;
        cout << res << endl;
    }
}
