class Solution:
    def search(self, nums: list[int], target: int) -> int:
        
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (hi + lo) // 2
            if nums[mid] > target:
                hi = mid - 1
            if nums[mid] < target:
                lo = mid + 1
            if nums[mid] == target:
                return mid

        return -1