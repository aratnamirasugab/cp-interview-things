#include <iostream>

using namespace std;

int decide(int n);

int main(void)
{
    long long x,y;

    int t;
    cin >> t;

    int check = 0;

    while(t != 0){

        cin >> x >> y;

        for(long long i = 2 ; i <= 1000000000000000000 ; i++){
            check = decide(i);
            if (check == 1){
                while( x != y){
                    x -= i;
                }
                if (x == y){
                    cout << "YES";
                }
            }else if (check == 0){
                cout << "NO";
            }
        }

        t--;
    }
}

int decide(int n)
{
    int i;
    for(i = 2 ; i < n ; i++){
        if (n % i == 0){
            return 0;
        }
    }
    if (i == n){
        return 1;
    }
}
