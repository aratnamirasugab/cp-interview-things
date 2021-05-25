//https://leetcode.com/problems/implement-strstr/
class Solution {
public:
    int strStr(string haystack, string needle) {

        if(needle.length() == 0){
            return 0;
        }

        if(needle.length() > haystack.length()) return -1;

        int match = 0;
        int temp = 0;
        int pointH = 0;

        for(int i = 0 ; i < haystack.length(); i++){
            if(haystack[i] == needle[0]){
                pointH = i;
                while(temp < needle.length()){
                    if(haystack[pointH] == needle[temp]){
                        match++;
                        pointH++;
                        temp++;
                    }
                }

                if(match == needle.length()){
                    return pointH - needle.length();
                }

            }
            temp = 0;
            match = 0;
        }

        return -1;

    }
};
