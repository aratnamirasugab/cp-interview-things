class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        data = sentence.split()
        for idx, item in enumerate(data):
            check = item.startswith(searchWord)
            if check == True:
                return idx
            
        return -1

if __name__ == '__main__':
    sentence = "i am tired"
    searchWord = "you"
    sol = Solution().isPrefixOfWord(sentence, searchWord)
    print(sol)

# Runtime: 32 ms, faster than 45.19% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
# Memory Usage: 14.2 MB, less than 43.42% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.