class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                if i == j:
                    continue
                if numbers[i] + numbers[j] == target:
                  return [i+1,j+1]

test_case = Solution()
ans = test_case.twoSum([1,1,2,4], 2)
print(ans)