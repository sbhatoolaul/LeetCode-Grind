class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, prefix_product, suffix, suffix_product = [], 1, [], 1

        for i in range(len(nums)):
            prefix_product *= nums[i]
            prefix.append(prefix_product)
            suffix_product *= nums[len(nums)-1-i]
            suffix.append(suffix_product)

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(suffix[-(i+2)])

            elif i == len(nums)-1:
                res.append(prefix[i-1])

            else:
                res.append(prefix[i-1] * suffix[-(i+2)])
        
        return res