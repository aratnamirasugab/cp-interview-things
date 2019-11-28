//https://leetcode.com/problems/longest-substring-without-repeating-characters
// UNSOLVED!!


#include <vector>
#include <algorithm>
#include <iterator>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int resMax = 0;
        vector<int> vec;
        vector<int> temp;

        for(int i = 0 ; i < s.length(); i++){
            if(find(vec.begin(), vec.end(), s[i]) == vec.end()){
                vec.push_back(s[i]);
            }else{
                if (vec.size() > resMax){
                    resMax = vec.size(); //3
                }

                if(s[i] == s[0]){
                    for(int j = 1 ; j < vec.size() ; j++){
                        temp.push_back(vec[j]);
                    }
                    vec.clear();
                    vec.assign(temp.begin(), temp.end());
                    temp.clear();
                }else if(s[i] != s[i-1]){
                    vec.clear();
                    vec.push_back(s[i-1]);
                    vec.push_back(s[i]);
                }else{
                    vec.clear();
                    vec.push_back(s[i]);
                }
            }
        }

        if (vec.size() > resMax)resMax = vec.size();

        return resMax;
    }
};
