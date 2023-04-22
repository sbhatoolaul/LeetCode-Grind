class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        most_freq = 0
        res = 0
        start = 0

        for end in range(len(s)):
            char = s[end]

            freq[char] = 1 + freq.get(char, 0)

            most_freq = max(most_freq, freq[char])
            
            if end+1-start-most_freq > k:
                # adjust window size
                freq[s[start]] -= 1
                start += 1

            res = max(res, end+1-start)
        
        return res
    