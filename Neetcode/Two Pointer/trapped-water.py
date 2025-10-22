class Solution:
    def trap(self, height: list[int]) -> int:
        waterCollected = 0
        leftMax = []
        rightMax = []

        prev = height[0]
        for i in height:
            leftMax.append(max(prev, i))
        prev = height[0]
        for i in range(len(height) - 1, -1, -1):
            rightMax.append(max(prev, height[i]))

        for idx, h in enumerate(height):
            if idx == 0 or idx == len(height) - 1:
                continue
            
            waterCollected += min(leftMax[idx], rightMax[idx]) - h
            
        return waterCollected
              
            
sol = Solution()
print(sol.trap([0,2,0,3,1,0,1,3,2,1]))