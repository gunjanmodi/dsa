class Solution:

    def longestSubstringWithKUniqueCharacters(self, s, k): # noqa
        d = dict()
        i = 0
        answer = 0
        for j in range(len(s)):
            d[s[j]] = d.get(s[j], 0) + 1
            if len(d) < k:
                pass
            elif len(d) == k:
                answer = max(answer, j - i + 1)
            elif len(d) > k:
                while len(d) > k and i <= j:
                    d[s[i]] -= 1
                    if d[s[i]] == 0:
                        del d[s[i]]
                    i += 1
        return answer if answer > 0 else -1
