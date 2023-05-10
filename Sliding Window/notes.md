# Study Notes:


### General Formats:

#### Fixed size sliding window


    def function(array):
        i, j =0, 0
        while j < len(array):
            Calculations
    
            if window size< k:
                j += 1
            elif window size == k: # calculate answer
                max_size = max(max_size, j - i + 1) # answer calculation
                # Remove calculation of i
                # Maintain window size and slide
                j += 1
        return answer`

#### Variable size sliding window


    def function(array):
        i, j =0, 0
        while j < len(array):
            Calculations
            if condition < k:
                j += 1
            elif condition == k: # calculate answer
                max_size = max(max_size, j - i + 1)
                j += 1
            elif condition > k:
                while condition > k: # Remove calculation of i
                    condition -= array[i]
                    i += 1
        return answer

##### Leetcode Articles:

1: [https://leetcode.com/tag/two-pointers/discuss/1122776/Summary-of-Sliding-Window-Patterns-for-Subarray-Substring](https://leetcode.com/tag/two-pointers/discuss/1122776/Summary-of-Sliding-Window-Patterns-for-Subarray-Substring)

2: [https://leetcode.com/discuss/study-guide/1773891/Sliding-Window-Technique-and-Question-Bank](https://leetcode.com/discuss/study-guide/1773891/Sliding-Window-Technique-and-Question-Bank)
