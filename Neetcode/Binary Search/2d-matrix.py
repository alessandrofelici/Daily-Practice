class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1
        lastCol = len(matrix[0]) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target > matrix[mid][lastCol]:
                lo = mid + 1
            if target < matrix[mid][lastCol]:
                hi = mid - 1
            if target <= matrix[mid][lastCol] and target >= matrix[mid][0]:
                return self.binarySearch(matrix[mid], target) != -1
            
        return False


    def binarySearch(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target > nums[mid]:
                lo = mid + 1
            if target < nums[mid]:
                hi = mid - 1
            if target == nums[mid]:
                return mid
        
        return -1