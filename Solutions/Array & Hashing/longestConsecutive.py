class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        nums = set(nums)

        for num in nums:
            if num-1 not in nums: # start of sequence
                i = 0
                while num+i in nums:
                    i += 1
                longest = max(longest, i)

        return longest