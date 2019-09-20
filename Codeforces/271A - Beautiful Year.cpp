#include <iostream>

using namespace std;

int main()
{
    int n, arr[5];

    cin >> n;

    n += 1;

    int a, res;
    for(int i = n ; i <= 9100 ; i++){
        int temp = i;
        a = 0;
        res = 0;
        while(temp > 0){
            arr[a] = temp % 10;
            temp /= 10;
            a++;
        }

        for(int x = 0 ; x < 4 ; x++){
            for(int y = 0 ; y < 4 ; y++){
                if (arr[x] == arr[y]){
                    res++;
                }
            }
        }

        if (res == 4){
            cout << i;
            return 0;
        }
    }
}
