#include <vector>
#include <algorithm>
#include <string>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> vec;
        int bMaxLength = 0;
        int aMaxLength = 0;

        for(int i = 0 ; i < s.length(); i++){
            if(find(vec.begin(), vec.end(), s[i]) == vec.end()){
                vec.push_back(s[i]);
                bMaxLength = vec.size();
            }else{
                vec.clear();
                bMaxLength = 1;
            }

            if(aMaxLength < bMaxLength){
                aMaxLength = bMaxLength;
            }
        }

        return aMaxLength;
    }
};
