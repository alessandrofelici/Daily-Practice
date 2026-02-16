class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r: int, c: int) -> int:
            area = 1
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            q = collections.deque()
            q.append((r,c))
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (r < rows and r >= 0
                        and c < cols and c >= 0
                        and grid[r][c] == 1
                        and (r, c) not in visited):
                        visited.add((r, c))
                        q.append((r,c))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                if ((r, c) not in visited and grid[r][c] == 1):
                    visited.add((r, c))
                    maxArea = max(maxArea, bfs(r, c)) 

        return maxArea
