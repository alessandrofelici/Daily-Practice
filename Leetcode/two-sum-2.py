class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            if sum > target:
                r -= 1
            if sum == target:
                return [l+1, r+1]
        
        return []

sol = Solution()
result = sol.twoSum([3,7,8,9], 10)
print(result)