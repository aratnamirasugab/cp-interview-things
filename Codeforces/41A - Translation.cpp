#include <bits/stdc++.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <string.h>

using namespace std;

int main(void)
{
    char str1[100], str2[100];
    cin >> str1;
    cin >> str2;

    //strlwr(str1);
    //strlwr(str2);

    char temp[100];
    int lengthStr2 = strlen(str2);

    for(int i = 0 ; i < lengthStr2 ; i++){
        temp[i] = str2[lengthStr2-(i+1)];
    }

    if (strcmp(str1, temp) == 0){
        cout << "YES";
    }
}
