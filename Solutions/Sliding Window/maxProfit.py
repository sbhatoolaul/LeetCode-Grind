class Solution(object):
    def maxProfit(self, prices):
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
        
        :type prices: List[int]
        :rtype: int
        """
        profit, lowest = 0, float('inf')

        for end in range(len(prices)):
            price = prices[end]
            profit = max(profit, price-lowest)

            lowest = min(lowest, price)

        return profit
        