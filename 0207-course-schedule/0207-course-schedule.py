class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        return (count==numCourses)






class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjlist=defaultdict(list)

        for x, y in prerequisites:
            adjlist[y].append(x)

        indegree=[0] *numCourses

        for i in range(numCourses):
            for nodes in adjlist[i]:
                indegree[nodes]+=1

        queue=deque()
        courselist=[]

        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            node=queue.popleft()
            courselist.append(node)

            for adjnodes in adjlist[node]:
                indegree[adjnodes]-=1
                if indegree[adjnodes]==0:
                    queue.append(adjnodes)

        return len(courselist)==numCourses







