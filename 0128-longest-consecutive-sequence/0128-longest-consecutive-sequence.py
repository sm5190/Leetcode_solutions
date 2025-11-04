class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        hashset=set(nums)
       

        
        i=0
        maxcount=1
        for num in hashset:
            
            if num-1 not in hashset:
                count=0
                
                while num+count in hashset:
                    count=count+1
  
                maxcount=max(count,maxcount)
        

        return maxcount
