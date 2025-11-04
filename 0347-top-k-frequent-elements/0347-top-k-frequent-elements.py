# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashmap={}
#         for i in nums:
#             if i in hashmap:
#                 hashmap[i]+=1
#             else:
#                 hashmap[i]=1
#         frequency=[(-freq, key) for key, freq in hashmap.items()]
        
#         # Step 1: Heapify the list to convert it into a min-heap (O(n))
#         heapq.heapify(frequency)
        
#         top_k = []  # To store the top k elements
#         for i in range(k-1):
#             top_k.append(heapq.heappop(frequency)[1])  # Store popped elements
        
#         print(frequency)  # This will contain the remaining elements after popping k
        
#         return top_k  # Return the list of top k elements


# Aditya's code.!!
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         result = []   
#         def get_frequency(nums): 
#             freq={}
#             for num in nums:
#                 if num in freq: 
#                     freq[num] += 1
#                 else: 
#                     freq[num] = 1
#             return freq
        
#         final_nums = get_frequency(nums)

#         for key, value in final_nums.items(): 
#             if value >= k:
#                 result.append(key)

#         return result 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #O(n+m+klogk)
        # hashmap=defaultdict(list)
        # for i in nums: #O(n)
            
        #     if i not in hashmap:
        #         hashmap[i]=[1, i]
        #     else:
        #        hashmap[i][0] += 1
            
       


        # freq=[(-f,i) for f, i in hashmap.values()] #O(m)
       

        # heapq.heapify(freq)
        # res=[]
        # for i in range(k): # k log k
        #     x=heapq.heappop(freq)
        #     res.append(x[1])
        # return res
        

## O(n)
        freq=Counter(nums)
        buckets=[[] for _ in range(len(nums)+1)]

        for num, f in freq.items():
            buckets[f].append(num)
        res=[]
        for f in range(len(nums), 0, -1):       # O(n)
            for num in buckets[f]:
                res.append(num)
                if len(res)==k:
                    return res

        return res

