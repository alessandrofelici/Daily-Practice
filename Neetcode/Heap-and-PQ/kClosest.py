import heapq
import math

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # variables
        # heapq in order of closest points/smallest distance from origin
        # dict to translate distance to points
        closestPoints = []
        distances = []
        heapq.heapify(distances)
        
        # for each point
        #   calc distance
        #   add distance to queue, with some map or pair that connects to points
        for point in points:
            distance = self.euclideanDistance(point)
            heapq.heappush(distances, [distance, point])

        # for k
        #   append to return set from pq
        #   return this set
        for i in range(k):
            closestPoints.append(heapq.heappop(distances)[1])

        return closestPoints
            
    
    def euclideanDistance(self, point: list[int]) -> int:
        return math.sqrt(point[0]**2 + point[1]**2)
    
sol = Solution()
print(sol.kClosest([[2,0],[2,2]], 2))