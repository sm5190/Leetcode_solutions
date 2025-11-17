class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        grid=[[0]*n for _ in range(n)]
        
        # for i in range(len(queries)):
        #     row1, col1, row2, col2= queries[i]

        #     for r in range(row1, row2+1):
        #         for c in range(col1, col2+1):
        #             grid[r][c]+=1

        # return grid
        diff=[[0]*(n+1) for _ in range(n+1)]
        for i in range(len(queries)):
            r1, c1, r2, c2=queries[i]
            diff[r1][c1]+=1
            diff[r1][c2+1]-=1
            diff[r2+1][c1]-=1
            diff[r2+1][c2+1]+=1

        for r in range(n):
            for c in range(n):
                top=0 if r==0 else grid[r-1][c]
                left=0 if c==0 else grid[r][c-1]
                top_left=0 if r==0 or c==0 else grid[r-1][c-1]
                grid[r][c]=diff[r][c]+top+left-top_left

        return grid

