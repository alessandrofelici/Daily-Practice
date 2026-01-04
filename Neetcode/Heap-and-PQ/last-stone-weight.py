import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        
        while len(stones) > 1:
            heapq.heapify_max(stones)

            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            x, y = x - y, y - x

            if x > 0:
                heapq.heappush_max(stones, x)
            if y > 0:
                heapq.heappush_max(stones, y)

        return 0 if not len(stones) else stones[0]

sol = Solution()
print(sol.lastStoneWeight([2,3,6,2,4]))