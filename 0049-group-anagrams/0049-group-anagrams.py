
###o(n klogk )
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        

        # hashmap=defaultdict(list)

        # for word in strs:
        #     x=''.join(sorted(word))
            
        #     hashmap[x].append(word)

        # print(hashmap)

        # return list(hashmap.values())

## 0(n, k)
        group=defaultdict(list)

        for word in strs:
            count=[0]* 26

            for ch in word:
                count[ord(ch)-ord('a')]+=1

            group[tuple(count)].append(word)

        return list(group.values())
