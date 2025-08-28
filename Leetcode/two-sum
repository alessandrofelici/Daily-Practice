class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash = {}
        
        # for curr in range(len(nums)):
        #     x = target - nums[curr]
        #     try:
        #         past_sol = hash[x]
        #         return [curr, past_sol]
        #     except KeyError:
        #         hash[nums[curr]] = curr

        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hash and hash[x] != i:
                return [hash[x], i]
        
        return []

        