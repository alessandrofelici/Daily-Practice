class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            sum = nums[i] + nums[j] + nums[k]
            while k != j:
                if sum > 0 and k > -1:
                    k -= 1
                if sum < 0 and j < len(nums):
                    j += 1
                if sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    break
                sum = nums[i] + nums[j] + nums[k]
            
        
        return triplets

nums = [-1,0,1,2,-1,-4]
sol = Solution()
triplets = sol.threeSum(nums)
print(triplets)