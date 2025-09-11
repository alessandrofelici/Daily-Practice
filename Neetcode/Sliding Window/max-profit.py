class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        
        min, maxDiff = prices[0], 0

        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > maxDiff:
                maxDiff = prices[i] - min

        return maxDiff

prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))