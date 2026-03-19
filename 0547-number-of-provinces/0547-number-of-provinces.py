from collections import deque
from typing import List

# class Disjoint:
    
#     def __init__(self,n):
#         self.rank=[0]*n
#         self.parent=[]
#         for i in range(n):
#             self.parent.append(i)

#     def findparent(self,u):
#         if self.parent[u]==u:
#             return u
#         self.parent[u]=self.findparent(self.parent[u])
#         return self.parent[u]

#     def unionbyrank(self,u,v):
#         u_u=self.findparent(u)
#         u_v=self.findparent(v)
#         if u_u==u_v:
#             return

#         if self.rank[u_u]<self.rank[u_v]:
#             self.parent[u_u]=u_v
#         elif self.rank[u_v]<self.rank[u_u]:
#             self.parent[u_v]=u_u
#         else:
#             self.parent[u_u]=u_v
#             self.rank[u_v]+=1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        # def bfs(start):
        #     queue = deque([start])
        #     while queue:
        #         node = queue.popleft()
        #         for neighbor in range(n):
        #             if isConnected[node][neighbor] == 1 and neighbor not in visited:
        #                 visited.add(neighbor)
        #                 queue.append(neighbor)

        def dfs(node):
            visited.add(node)
            for neighbour in range(n):
                if isConnected[node][neighbour]==1 and neighbour not in visited:
                    dfs(neighbour)


        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces
        # ds=Disjoint(n)
        # cnt=0
        # for i in range(n):
        #     for j in range(n):
        #         if isConnected[i][j]==1:
        #             ds.unionbyrank(i, j)

        # for r in range(n):
        #     if ds.findparent(r)==r:
        #         cnt+=1
                   

        # return cnt