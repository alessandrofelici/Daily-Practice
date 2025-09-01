class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r, maxArea = 0, len(heights) - 1, 0
        while l < r:
          currArea = min(heights[l], heights[r]) * (r - l)
          maxArea = max(maxArea, currArea)

          if heights[l] < heights[r]:
              l += 1
          else:
              r -= 1

        return maxArea

sol = Solution()
print(sol.maxArea([1,7,2,5,4,7,3,6]))