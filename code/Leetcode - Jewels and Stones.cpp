// https://leetcode.com/problems/jewels-and-stones/
Runtime: 4 ms, faster than 65.04% of C++ online submissions for Jewels and Stones.
Memory Usage: 8.5 MB, less than 48.75% of C++ online submissions for Jewels and Stones.

#include <algorithm>
#include <vector>

class Solution {
public:
    int numJewelsInStones(string J, string S) {

        int result = 0;

        for (int i = 0 ; i < S.length(); i++){
            if(find(J.begin(), J.end(), S[i]) != J.end()){
                result++;
            }
        }

        return result;
    }
};
