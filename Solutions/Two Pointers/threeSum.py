class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)

        res = []
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                res.extend(self.twoSum(nums, i+1, -nums[i]))

        return res

    def twoSum(self, nums, start, target):

        res = []

        end = len(nums)-1

        while start < end:
            if nums[start] + nums[end] < target:
                start += 1

            elif nums[start] + nums[end] > target:
                end -= 1

            else: # nums[start] + nums[end] == target:
                # add to res
                res.append([-target, nums[start], nums[end]])

                # skip over duplicates
                while start < end and nums[start] == res[-1][1]:
                    start += 1

                while start < end and nums[end] == res[-1][-1]:
                    end -= 1

        return res