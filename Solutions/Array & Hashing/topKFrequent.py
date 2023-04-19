class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        memory = {}
        buckets = [[] for i in range(len(nums))] # max we can get is a character appearing all len(nums) times

        for num in nums:
            memory[num] = 1 + memory.get(num, 0)

            buckets[memory[num]-1].append(num)
        

        for i in reversed(range(len(buckets))):
            if len(buckets[i]) == k:
                return buckets[i]
        return []
        
        