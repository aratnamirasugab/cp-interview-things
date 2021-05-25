https://leetcode.com/problems/reverse-integer/
// MY APPROACH < DIDN'T HANDLE IF NUMBER TOO LARGE
#include <algorithm>
#include <vector>
class Solution {
public:
    int reverse(int x) {
        vector<int> vec;
        bool neg = false;
        int result = 0;

        if(x<0){
            neg = true;
            x = x * -1;
        }

        while(x > 0){
            vec.push_back(x%10);
            x = x/10;
        }

        for(int i = 0 ; i < vec.size(); i++){
            result *= 10;
            result += vec[i];
        }

        if(neg == true){
            result = result * -1;
        }

        return result;
    }
};

//ANOTHER APPROACH
Runtime: 0 ms, faster than 100.00% of C++ online submissions for Reverse Integer.
Memory Usage: 8.2 MB, less than 89.52% of C++ online submissions for Reverse Integer.
class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;
            if (rev > INT_MAX/10 || (rev == INT_MAX / 10 && pop > 7)) return 0;
            if (rev < INT_MIN/10 || (rev == INT_MIN / 10 && pop < -8)) return 0;
            rev = rev * 10 + pop;
        }
        return rev;
    }
};
