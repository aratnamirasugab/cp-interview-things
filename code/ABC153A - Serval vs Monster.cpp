//https://atcoder.jp/contests/abc153/tasks/abc153_a

#include <iostream>
#include <cmath>

using namespace std;

// first approach
int main(void)  {
    int H, A;
    cin >> H >> A;
    int t = 0;

    while (H > 0) {
        H -= A;
        t++;
    }

    cout << t << endl;
}

//second approach
int main(void) {
    float H, A;
    cin >> H >> A;
    cout << ceil(H/A) << endl;
}