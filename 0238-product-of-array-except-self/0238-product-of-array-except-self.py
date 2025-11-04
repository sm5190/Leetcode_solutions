# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         r=[1]*len(nums)
#         prefix=1
#         suffix=1
#         for i in range(len(nums)):
#             r[i]=prefix
#             prefix=prefix*nums[i]
#         print(r)
#         for j in range(len(nums)-1,-1,-1):
#             r[j]=r[j]*suffix
#             suffix=suffix*nums[j]
            
#         print(r) 
        
        

        
            
#         return r



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Left prefix product
        pref = 1
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        
        # Right suffix product
        suff = 1
        for i in range(n-1, -1, -1):
            res[i] *= suff
            suff *= nums[i]
        
        return res





