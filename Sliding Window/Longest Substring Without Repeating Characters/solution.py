class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: # noqa
        i = 0
        chars = {}
        max_window_size = 0
        for j in range(len(s)):
            chars[s[j]] = chars.get(s[j], 0) + 1
            if chars[s[j]] > 1:
                while chars[s[j]] > 1:
                    chars[s[i]] -= 1
                    i += 1
            max_window_size = max(max_window_size, j - i + 1)
        return max_window_size
