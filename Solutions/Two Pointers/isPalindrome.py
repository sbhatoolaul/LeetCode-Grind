class Solution(object):
    def isAlphaNumeric(self, char):
        return 'a' <= char <= 'z' or '0' <= char <= '9'   

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()

        start, end = 0, len(s)-1

        while start < end:

            while start < end and not self.isAlphaNumeric(s[start]):
                start += 1

            while start < end and not self.isAlphaNumeric(s[end]):
                end -=1

            if s[start] != s[end]:
                return False

            start += 1
            end -= 1

        return True

    # # Easier, but less space-efficient, I guess
    # def isPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     s = ''.join([char for char in s.lower() if self.isAlphaNumeric(char)])
    #     return s == s[::-1]