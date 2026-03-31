import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:

        heapq.heapify_max(nums)

        num = 0
        while k > 0:
            num = heapq.heappop_max(nums)
            k -= 1

        return num


sol = Solution()
result = sol.findKthLargest([3, 2, 1, 5, 6, 4], 2)
print(result)
