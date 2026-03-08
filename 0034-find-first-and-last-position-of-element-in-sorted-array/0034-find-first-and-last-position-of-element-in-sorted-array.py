class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l=0
        r=len(nums)-1
        i=-1
        def bs(l,r,i, leftbias):
            while(l<=r):
                mid=(l+r)//2
                if nums[mid]< target:
                    l=mid+1
                elif nums[mid]>target:
                    r=mid-1
                else:
                    i=mid
                    if leftbias:
                        r=mid-1
                    else:
                        l=mid+1
            return i
        
        left=bs(l, r, i, True)
        right=bs(l, r, i, False)

        return [left, right]



# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]: 
#         def FindFirst( nums, target):
#             left=0 #5
#             right=len(nums)-1 #10
#             ans=-1
#             while left<=right: 
#                     print((left, right))
#                     mid=(left+right)//2 
#                     if nums[mid]==target:
#                             ans=mid 
#                             right=mid-1 
#                     elif nums[mid]<target:
#                         left=mid+1
                            
#                     else:
#                         right=mid-1
#             return ans
            
#             def FindLast(nums, target):

#                 left=0
#                 right=len(nums)-1
#                 ans=-1
#                 while left<=right:
#                         print((left, right))
#                         mid=(left+right)//2
#                         if nums[mid]==target:
#                                 ans=mid
#                                 left=mid+1 
#                         elif nums[mid]<target:
#                             left=mid+1
                                
#                         else:
#                             right=mid-1
#                 return ans
                
#             first= findFirst(nums, target)
#             last= findLast(nums, target)
#             return [first, last]

    



        