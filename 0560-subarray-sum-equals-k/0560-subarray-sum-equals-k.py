class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
    

        # i=0
        # count=0
        # while i<len(nums):
        #     j=i+1
        #     sum=nums[i]
        #     while j<len(nums)  and sum!=k:
        #         sum=sum+ nums[j]
            
        #         j=j+1
        #     if sum==k:
        #         count=count+1
        #     i=i+1
        
        # return count

        prefix={0:1}
        csum=0
        res=0
        for i in range(len(nums)):
            csum=csum+nums[i]
            if (csum-k) in prefix:
                res=res+ prefix[(csum-k)]
        
            if csum in prefix:
                prefix[csum]+=1
            else:
                prefix[csum]=1
        return res
            

