class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # dict
        #   {temp: index}
        # get days since curr - index
        # append
        # dont do this bc want order based

        # loop through each elem
        # check stack and remove if greater
        stack = []
        days = [(0,0)] * len(temperatures)
        for day, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                days[stack[-1][1]] = day - stack[-1][1]
                stack.pop()
            else:
                stack.append((temp, day))
        
        while stack:
            days[stack[-1][1]] = 0
            stack.pop()
        
        return days

sol = Solution()
print(sol.dailyTemperatures([30,38,30,36,35,40,28]))

# stack (30,0) 
# days