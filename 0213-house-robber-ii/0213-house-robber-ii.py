class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        ans1= self.dp(nums[1:]) #leaving 1st
        ans2=self.dp(nums[: len(nums)-1]) #leaving last

        # #leaving 1st element
        # prev2=0
        # prev=nums[1]

        # for i in range(2, len(nums)):
        #     take=nums[i]+prev2
        #     non_take=0+prev
        #     curri=max(take, non_take)
        #     prev2=prev
        #     prev=curri
        # ans1=prev


        # #leaving last element
        # prev2=0
        # prev=nums[0]

        # for i in range(1, len(nums)-1):
        #     take=nums[i]+prev2
        #     non_take=0+prev
        #     curri=max(take, non_take)
        #     prev2=prev
        #     prev=curri

        # ans2=prev

        return max(ans1, ans2)


    def dp(self, nums):
        prev2=0
        prev=nums[0]

        for i in range(1, len(nums)):
            take=nums[i]+prev2
            non_take=0+prev
            curri=max(take, non_take)
            prev2=prev
            prev=curri

        return prev




            