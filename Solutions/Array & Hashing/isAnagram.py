class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # know it's same length, iterate through both
        smemory = {}
        tmemory = {}

        for i in range(len(s)):  # or len(t)
            smemory[s[i]] = 1 + smemory.get(s[i], 0)
            tmemory[t[i]] = 1 + tmemory.get(t[i], 0)

        return smemory == tmemory