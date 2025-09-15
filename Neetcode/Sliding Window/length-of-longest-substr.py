class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        maxLen, currLen, beginning = 0, 0, 0
        prev = s[0]
        hash = {}
        
        for index, char in enumerate(s):
            if char in hash and hash[char] >= beginning:
                maxLen = max(maxLen, currLen)
                beginning = hash[char] + 1
                currLen = index - beginning
                print(currLen)
                del hash[char]
            if prev == char:
                currLen = 0
            hash[char] = index
            currLen += 1
            print(hash, currLen)
            prev = char

        return max(maxLen, currLen)

sol = Solution()
print(sol.lengthOfLongestSubstring("aaca"))
# print(sol.lengthOfLongestSubstring("thequickbrownfoxjumpsoverthelazydogthequickbrownfoxjumpsovert"))