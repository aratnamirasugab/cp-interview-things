#include <iostream>

using namespace std;

class solution{

    public :

        int power(int x, int y)
        {
            if(y == 0){
                return 1;
            }else if(y % 2 == 0){
                return power(x, y/2) * power(x, y/2);
            }else{
                return x * power(x, y/2) * power(x, y/2);
            }
        }
};

int main(void)
{
    solution s;
    int number, pow;
    cin >> number >> pow;

    int res = s.power(number, pow);
    cout << number << " to the power of " << pow << " is : " << res;
}
