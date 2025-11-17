class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n= len(heights)
        m=len(heights[0])
        if n<1 or m<1:
            return []
        
        directions=[[+1, 0], [-1, 0], [0, 1], [0, -1]]
        pacific_queue=deque()
        atlantic_queue=deque()
        for i in range(m):
            pacific_queue.append((0,i))
            atlantic_queue.append((n-1, i))

        for j in range(n):
            pacific_queue.append((j, 0))
            atlantic_queue.append((j, m-1))
        
       
        def bfs(queue):
            reachable=set()
            
            while queue:
                r,c= queue.popleft()
                reachable.add((r,c))

                for dr, dc in directions:
                    nr= r+dr
                    nc=c+dc

                    if 0<=nr<n and 0<=nc<m  and (nr, nc ) not in reachable:
                        if heights[nr][nc]>=heights[r][c]:

                            queue.append((nr, nc))

            return reachable

        pacific_reachable = bfs(pacific_queue)
        atlantic_reachable = bfs(atlantic_queue)
        
        # Find all cells that can reach both oceans, and convert to list
        return list(pacific_reachable.intersection(atlantic_reachable))

                
                            

                        
                            
                


        



        
