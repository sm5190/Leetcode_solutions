class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        count=0
        minlen=float("inf")
        hashmap={}
        sindex=-1

        for c in t:
            if c not in hashmap:
                hashmap[c]=1
            else:
                hashmap[c]+=1



        while r<len(s):
            if s[r] in hashmap:
                if hashmap[s[r]]>0:
                    count+=1
                hashmap[s[r]]-=1
                    
                    
            while count==len(t):
                if r-l+1 < minlen:
                    minlen=r-l+1
                    sindex=l
                if s[l] in hashmap:
                    hashmap[s[l]] += 1
                    if hashmap[s[l]] > 0:
                        count -= 1
                l=l+1

            r=r+1

        return "" if sindex==-1 else s[sindex:sindex+minlen]

            

            