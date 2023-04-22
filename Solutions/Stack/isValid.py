class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parantheses = {'(': ')',
                       '[': ']',
                       '{': '}'
                     }

        stack = []

        for char in s:
            if char in parantheses:
                stack.append(char)
            else:
                if not stack or char != parantheses[stack.pop()]:
                    return False

        return not stack