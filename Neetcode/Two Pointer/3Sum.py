class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while k > j:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                if sum < 0:
                    j += 1
                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        l += 1
            
        return triplets

nums = [-1,0,1,2,-1,-4]
sol = Solution()
triplets = sol.threeSum(nums)
print(triplets)