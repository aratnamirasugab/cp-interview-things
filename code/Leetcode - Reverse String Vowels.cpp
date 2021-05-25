//https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
public:
    string reverseVowels(string s) {
       int start = 0;
        int end = s.size()-1;

        while(start < end){
            while(isVowel(s[start]) == false && start < end) start++;
            while(isVowel(s[end]) == false && start < end) end--;
            swap(s[start++], s[end--]);
        }
        return s;
    }

private :
    bool isVowel(char &c)
    {
        bool flag = false;
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' ||  c == 'I' || c == 'O' || c == 'U'){
            flag = true;
        }

        return flag;
    }
};
