//https://leetcode.com/problems/longest-substring-without-repeating-characters
// UNSOLVED!!


#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int resMax = 0;
        vector<int> vec;

        for(int i = 0 ; i < s.length(); i++){
            if(find(vec.begin(), vec.end(), s[i]) == vec.end()){
                vec.push_back(s[i]);
            }else{
                if (vec.size() > resMax){
                    resMax = vec.size(); //3
                }
                vec.clear();
                if(s[i] != s[i-1]){
                    vec.push_back(s[i-1]);
                    vec.push_back(s[i]);
                }else{
                    vec.push_back(s[i]);
                }
            }
        }

        if (vec.size() > resMax)resMax = vec.size();

        return resMax;
    }
};
