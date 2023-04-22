class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needed = {}
        for char in t:
            needed[char] = 1 + needed.get(char, 0)
        
        matches, start, minimum = 0, 0, ""

        for end in range(len(s)):
            char = s[end]

            if char in needed:
                needed[char]-=1
                if needed[char] == 0:
                    matches += 1

            while matches == len(needed): # we found everything in t
                if minimum == "" or end+1-start < len(minimum):
                    minimum = s[start:end+1]

                # try to shrink window further
                if s[start] in needed:
                    needed[s[start]] += 1
                    if needed[s[start]] > 0:
                        matches -= 1

                start += 1


        return minimum
          