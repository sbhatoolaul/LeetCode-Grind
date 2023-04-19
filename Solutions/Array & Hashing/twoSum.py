class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # More time-efficient (O(n))
        memory = {}  # key = nums[i], value = i (location in i)
    
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in memory:
                return [memory[needed], i]

            memory[nums[i]] = i

        # More space-efficient (O(1)), but doesn't work for this one because we need indices
        # nums = sorted(nums)

        # left = 0
        # right = len(nums)-1

        # while 1:  # we know there is always exactly one solution
        #     if nums[left] + nums[right] > target:
        #         right -= 1
        #     elif nums[left] + nums[right] < target:
        #         left += 1
        #     else:
        #         return [left, right]
