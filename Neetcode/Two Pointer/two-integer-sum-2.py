class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        min, max = 0, len(numbers)-1

        while min < max:
            curSum = numbers[min] + numbers[max]
            if curSum > target:
                max -= 1
            if curSum < target:
                min += 1
            if curSum == target:
                return [min+1, max+1]
            
        return []

test_case = Solution()
ans = test_case.twoSum([0,0,0,1,2,4,4], 3)
print(ans)