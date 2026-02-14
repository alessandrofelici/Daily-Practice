class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def bfs(i, j):
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for di, dj in directions:
                    i, j = row + di, col + dj
                    if ((i) in range(rows) and
                        (j) in range(cols) and
                        grid[i][j] == "1" and
                        (i, j) not in visited):
                        q.append((i, j))
                        visited.add((i, j))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1

        return islands