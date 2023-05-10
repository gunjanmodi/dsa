class Solution:
    """
    Algorithm: Sliding Window
    Category: Variable size sliding window


    Problem Link: https://leetcode.com/problems/longest-repeating-character-replacement

    This can be thought of as, Longest substring where (count of most frequent character) + k < length.

    Explanation:
        end-start+1 = size of the current window
        maxCount = largest count of a single, unique character in the current window

        The main equation is: end-start+1-maxCount

        When end-start+1-maxCount == 0, then then the window is filled with only one character
        When end-start+1-maxCount > 0, then we have characters in the window that are NOT the character that occurs the
         most.
        end-start+1-maxCount is equal to exactly the # of characters that are NOT the character that occurs the most in
         that window. Example: For a window "xxxyz", end-start+1-maxCount would equal 2.
        (maxCount is 3 and there are 2 characters here, "y" and "z" that are not "x" in the window.)

        We are allowed to have at most k replacements in the window, so when end-start+1-maxCount > k,
         then there are more characters in the window than we can replace, and we need to shrink the window.

         If we have window with "xxxy" and k = 1, that's fine because end-start+1-maxCount = 1,
         which is not > k. maxLength gets updated to 4.

         But if we then find a "z" after, like "xxxyz", then we need to shrink the window because now
          end-start+1-maxCount = 2, and 2 > 1. The window becomes "xxyz".

        maxCount may be invalid at some points, but this doesn't matter, because it was valid earlier in the string,
         and all that matters is finding the max window that occurred anywhere in the string. Additionally,
          it will expand if and only if enough repeating characters appear in the window to make it expand.

        So whenever it expands, it's a valid expansion.

    Complexity Analysis:
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    def characterReplacement(self, s: str, k: int) -> int: # noqa
        i = j = 0
        d = {}
        answer = 0
        max_char_count = 0
        while j < len(s):
            d[s[j]] = d.get(s[j], 0) + 1
            max_char_count = max(max_char_count, d[s[j]])
            window_size = j - i + 1

            if window_size - max_char_count > k:
                d[s[i]] -= 1
                i += 1

            answer = max(answer, j - i + 1)
            j += 1
        return answer
