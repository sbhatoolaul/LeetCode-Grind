class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Given a string s, find the length of the longest substring without repeating characters.

        :type s: str
        :rtype: int
        """
        longest, start, seen = 0, 0, set()

        for end in range(len(s)):    
            char = s[end]

            while char in seen:

                if s[start] in seen:
                    seen.remove(s[start])
                start += 1

            seen.add(char)
            longest = max(longest, end+1-start)

        return longest
