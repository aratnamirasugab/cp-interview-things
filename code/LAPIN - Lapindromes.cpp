//https://www.codechef.com/problems/LAPIN

#include <bits/stdc++.h>

using namespace std;

bool checkIsLapalindrome(string s1, string s2)
{
    for(int i = 0 ; i < s1.length() ; i++){
        if(s1[i] != s2[i]){
                return false;
        }
    }

    return true;
}

int main(void)
{
    string S;
    int T;
    cin >> T;

    while(T > 0)
    {
        cin >> S;
        string str1,str2;

        int start = 0;
        int end = S.length()-1;

            while(start < end){
                str1.push_back(S[start]);
                str2.push_back(S[end]);
                start++; end--;
            }

            sort(str1.begin(), str1.end());
            sort(str2.begin(), str2.end());

            bool res = checkIsLapalindrome(str1, str2);

            if(res == true){
                cout << "YES\n";
            }else{
                cout << "NO\n";
            }

        str1.clear(); str2.clear();
        T--;
    }

}
