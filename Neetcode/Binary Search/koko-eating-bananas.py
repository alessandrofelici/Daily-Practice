class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        k_min, k_curr = float('inf'), 0
        lo, hi = 1, max(piles)
        while lo <= hi:
            k_curr = (lo+hi)//2
            hours = 0
            for j in range(len(piles)):
                hours += piles[j]//k_curr
                if piles[j]%k_curr != 0:
                    hours += 1
            # print(k_curr, hours)
            if hours <= h:
                k_min = min(k_min, k_curr)
                hi = k_curr - 1
            else:
                lo = k_curr + 1

        return k_min
    
sol = Solution()
print(sol.minEatingSpeed([1,4,3,2], 9))
print(sol.minEatingSpeed([25,10,23,4], 4))
print(sol.minEatingSpeed([3,6,7,11], 8))
print(sol.minEatingSpeed([312884470], 312884469))