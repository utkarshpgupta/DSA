# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        count = 0
        substr = set()
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            substr.add(s[r])
            count = max(count, r - l + 1)
        print(substr)
        return count