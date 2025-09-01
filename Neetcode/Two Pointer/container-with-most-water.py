class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r, maxArea = 0, len(heights) - 1, 0
        while l < r:
          width = r - l
          currArea = min(heights[l], heights[r]) * width
          
          if currArea > maxArea:
              maxArea = currArea

          if heights[l] < heights[r]:
              l += 1
          elif heights[r] < heights[l]:
              r -= 1
          elif heights[r] == heights[l]:
              r -= 1

        return maxArea

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))