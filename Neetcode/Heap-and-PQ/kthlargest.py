import heapq
import math

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        nums = self.nums
        while len(nums) > self.k:
            heapq.heappop(nums)
        return nums[0]

        
sol = KthLargest(3, [4, 5, 8, 2])
print(sol.add(3))
print(sol.add(5))