import math

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        
        pair = [[p,s] for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        print(pair)
        # O(n) space
        stack = []

        # O(n) time
        for car, data in enumerate(pair):
          if stack:
            prevCar = stack[-1]
            prevPos = pair[prevCar][0]
            pos = pair[car][0]
            prevTime = ((target - prevPos)/pair[prevCar][1])
            time = ((target - pos)/pair[car][1])

            if time > prevTime:
              stack.append(car)
          else:
            stack.append(car)
          
          print(stack, car)

        return len(stack)

sol = Solution()
print(sol.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]))