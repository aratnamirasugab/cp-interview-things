#include <iostream>
#include <vector>

using namespace std;

void reverseString(vector<char>& s) {

    for(int i = 0 ; i < s.size(); i++){
        for(int j = 0 ; j < s.size(); j++){
            s[i] = int(s[i]) + int(s[j]);
            s[j] = int(s[i]) - int(s[j]);
            s[i] = int(s[i]) - int(s[j]);
        }
    }

    for(int i = 0 ; i < s.size(); i++){
        cout << s[i] << " ";
    }
}

int main(void)
{
    vector<char> vec;
    vec.push_back('h');
    vec.push_back('e');
    vec.push_back('l');
    vec.push_back('l');
    vec.push_back('o');

    reverseString(vec);
}
