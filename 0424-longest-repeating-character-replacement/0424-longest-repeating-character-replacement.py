class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf=0
        maxl=0
        l=0
        r=0
        charmap={}
        while r<len(s):
            if s[r] not in charmap:
                charmap[s[r]]=1
            else:
                charmap[s[r]]+=1
            maxf=max(maxf, charmap[s[r]])

            if (r-l+1)-maxf>k:
                charmap[s[l]]-=1
                if charmap[s[l]]==0:
                    del charmap[s[l]]
                l=l+1

            else:
                maxl=max(maxl, r-l+1)
            r=r+1

        return maxl
