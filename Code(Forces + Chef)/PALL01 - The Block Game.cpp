//https://www.codechef.com/problems/PALL01

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
    int T;
    cin >> T;
    int N = 0;
    vector<int> vec;

    while(T > 0)
    {
        cin >> N;

        while(N > 0)
        {
            vec.push_back(N % 10);
            N /= 10;
        }

        int start = 0;
        int end = vec.size()-1;
        int pal = true;

        while(start < end){
            if(vec[start] != vec[end]) pal = false;
            start++; end--;
        }

        if(pal == true){
            cout << "wins\n";
        }else{
            cout << "losses\n";
        }

        vec.clear();
        T--;
    }
}
