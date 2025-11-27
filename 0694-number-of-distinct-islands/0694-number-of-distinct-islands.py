class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinct=set()
        visit=set()
        n=len(grid)
        m=len(grid[0])
        def dfs(r,c, base_r, base_c,shape):
            visit.add((r,c))
            shape.append((r-base_r, c-base_c))

            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                n_r=r+dr
                n_c=c+dc

                if n_r<n and n_c<m and n_r>=0 and n_c>=0 and (n_r, n_c) not in visit and grid[n_r][n_c]==1:
                    visit.add((n_r,n_c))
                   
                    dfs(n_r, n_c,base_r, base_c,shape )


        for i in range(n):
            for j in range(m):
                if (i,j) not in visit and grid[i][j]==1:
                        shape=[]
                        dfs(i,j, i,j, shape)
                        distinct.add(tuple(shape))
        print(distinct)
        return len(distinct)




 

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinct=set()
        n= len(grid)
        m=len(grid[0])

        visit=set()
        directions=[[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j ,base_i, base_j, shape):
            visit.add((i, j))
            shape.append((i-base_i,j-base_j))
            for dr, dc in directions:
                nr= i+dr
                nc= j+dc

                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==1 and (nr,nc) not in visit:
                    
                    dfs(nr, nc, base_i, base_j, shape)
                    
        
        for r in range(n):
            for c in range(m):
                if (r, c) not in visit and grid[r][c]==1:
                    shape =[]
                    dfs(r, c, r, c, shape)

                    distinct.add(tuple(shape))

        print(distinct)
        return len(distinct)
                    




















