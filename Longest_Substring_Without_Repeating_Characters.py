class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            current = ""
            for j in range(i, len(s)):
                if s[j] not in current:
                    current += s[j]
                else:
                    break
            if len(current) > max_length:
                max_length = len(current)
        return max_length