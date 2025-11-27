# from collections import defaultdict, deque
# from typing import List

# class Solution:
#     def alienOrder(self, words: List[str]) -> str:
#         adj = defaultdict(list)
#         indegree = {}  # only store existing chars

#         # Step 1: Initialize all characters with indegree 0
#         for word in words:
#             for c in word:
#                 indegree[c] = 0

#         # Step 2: Build the graph
#         for i in range(1, len(words)):
#             w1, w2 = words[i-1], words[i]
#             min_len = min(len(w1), len(w2))

#             # Check for invalid case like ["abc", "ab"]
#             if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
#                 return ""

#             for j in range(min_len):
#                 if w1[j] != w2[j]:
#                     adj[w1[j]].append(w2[j])
#                     indegree[w2[j]] += 1
#                     break  # only first diff matters

#         # Step 3: Topological sort (Kahn's algorithm)
#         queue = deque([c for c in indegree if indegree[c] == 0])
#         topo_order = []

#         while queue:
#             node = queue.popleft()
#             topo_order.append(node)

#             for neighbor in adj[node]:
#                 indegree[neighbor] -= 1
#                 if indegree[neighbor] == 0:
#                     queue.append(neighbor)

#         # Step 4: If all chars are included, return result
#         if len(topo_order) == len(indegree):
#             return "".join(topo_order)
#         else:
#             return ""  # Cycle detected or invalid input






class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjlist=defaultdict(list)
        indegree={}

        
        for word in words:
            for ch in word:
                indegree[ch]=0


        for i in range(1, len(words)):
            word1=words[i-1]
            word2= words[i]
            minlen=min(len(word1), len(word2))

            
            if word1[:minlen] == word2[:minlen] and len(word1) > len(word2):
                return ""
            for j in range(minlen):
                if word1[j]!=word2[j]:
        
                    adjlist[word1[j]].append(word2[j])
                    indegree[word2[j]]+=1
                    break
        
        print(adjlist)
        queue=deque()
        for ch in indegree:
            if indegree[ch]==0:
                queue.append(ch)
        print(queue)
        res=[]
        while queue:
            char=queue.popleft()
            res.append(char)

            for adjnodes in adjlist[char]:
                indegree[adjnodes]-=1
                if indegree[adjnodes]==0:
                    queue.append(adjnodes)

        return "".join(res) if len(res)==len(indegree) else ""
        


        



        


        





