class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj=defaultdict(list)
        indegree=[0]* numCourses
        queue=deque()

        for c1,c2 in prerequisites:
            adj[c2].append(c1)

        for i in range(numCourses):
            for adj_nodes in adj[i]:
                indegree[adj_nodes]+=1

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        count=0
        topo=[]
        while queue:
            node=queue.popleft()
            topo.append(node)
            count+=1

            for adj_nodes in adj[node]:
                indegree[adj_nodes]-=1
                if indegree[adj_nodes]==0:
                    queue.append(adj_nodes)
        print(topo)
        return topo if (count==numCourses) else []


