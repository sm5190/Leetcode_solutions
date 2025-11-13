class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        adjlist=defaultdict(list)
        MOD = 10**9 + 7
        res=[0]* (len(conversions)+1)

        for s, t, f in conversions:
            adjlist[s].append((t, f))

        print(adjlist)
        queue=deque()
        queue.append(0)
        res[0]=1

        while queue:
            t=queue.popleft()
            for node, weight in adjlist[t]:
                res[node]=(res[t] * weight)%MOD

                queue.append(node)

        return res
            