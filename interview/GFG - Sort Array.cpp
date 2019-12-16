#include <iostream>
#include <algorithm>

using namespace std;

int main(void)
{
    string str = "111122211111";

    for(int i = 0 ; i < str.length(); i++){
        for(int j = 0 ; j < str.length(); j++){
            if(str[i] < str[j]){
                swap(str[i], str[j]);
            }
        }
    }

    cout << "String str is : " << str;
}
