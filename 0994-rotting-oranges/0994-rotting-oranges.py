

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        # Step 1: Collect all initial rotten oranges
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        # Step 2: BFS to rot neighbors
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Rot it
                    fresh -= 1
                    queue.append((nr, nc, t + 1))

        # Step 3: Check if all fresh oranges are rotted
        return time if fresh == 0 else -1









class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n=len(grid)
        m=len(grid[0])

        queue= deque()

        fresh=0

        for r in range(n):
            for c in range(m):
                if grid[r][c]==2:
                    queue.append((r, c, 0))

                elif grid[r][c]==1:
                    fresh+=1

                else:
                    continue

        time=0
        directions=[[1, 0], [-1, 0], [0, -1], [0, 1]]

        T=0
        while queue:
            row, col, time= queue.popleft()
            T= max(time, T)
            
            for dr, dc in directions:
                nr= row+dr
                nc= col+dc

                if 0<=nr<n and 0<=nc<m and grid[nr][nc]!=0:
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                        fresh-=1

                        queue.append((nr, nc, time+1))

        return T if fresh==0 else -1



















