#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    vector <int> vec;

    cout << "Batas primer number : ";
    int n;
    cin >> n;

    for(int i = 2 ; i < n ; i++){
        if (i % i == 0 && i & 1 == 0){
            vec.push_back(i);
        }
    }

    cout << "\n";
    for(int i = 0; i < vec.size(); i++){
        cout << vec[i];
    }
}
