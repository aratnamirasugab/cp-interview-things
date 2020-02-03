#include <iostream>

using namespace std;

int main(void)
{
    int n;
    cin >> n;

    int p,q;
    int totalRoom = 0;

    for (int i = 0 ; i < n ; i++){
        cin >> p >> q;
        if (p <= q-2) totalRoom++;
    }

    cout << totalRoom;

}
