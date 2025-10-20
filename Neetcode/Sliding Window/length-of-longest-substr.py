class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l, r = 0, 0
        longest = 0
        charSet = set()

        while r < len(s):
            while s[r] in set:
                charSet.remove(s[l])
                l += 1
            
            charSet.add(s[r])

            longest = max(longest, r - l + 1)

            r += 1

        return longest