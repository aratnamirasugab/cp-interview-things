//https://leetcode.com/problems/palindrome-number/
Runtime: 20 ms, faster than 31.98% of C++ online submissions for Palindrome Number.
Memory Usage: 7.9 MB, less than 100.00% of C++ online submissions for Palindrome Number.
class Solution {
public:
    bool isPalindrome(int x) {
        int temp = x;
        int res = 0;

        if(temp < 0){
            return false;
        }

        while(temp != 0){
            if (res > INT_MAX/10 || (res == INT_MAX / 10 && temp > 7)) return false;
            if (res < INT_MIN/10 || (res == INT_MIN / 10 && temp < -8)) return false;
            res = res*10 + temp%10;
            temp /= 10;
        }

        if(res == x)return true;
        else return false;
    }
};
