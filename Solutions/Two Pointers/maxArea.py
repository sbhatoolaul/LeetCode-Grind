class Solution(object):
    def getArea(self, height, start, end):
        return min(height[start], height[end]) * (end-start)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height)-1

        maximum = 0
        while start < end:
            maximum = max(maximum, self.getArea(height, start, end))

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maximum