class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        groups = {}

        for word in strs:
            freq = [0] * 26 # freq[0] = frequency of 'a', freq[1] = frequence of 'b', etc..

            for letter in word:
                freq[ord(letter)-ord('a')] += 1

            if tuple(freq) not in groups:
                groups[tuple(freq)] = []
            groups[tuple(freq)].append(word)

        return [groups[group] for group in groups]