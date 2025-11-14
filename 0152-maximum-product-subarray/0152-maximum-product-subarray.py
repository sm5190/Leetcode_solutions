class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # maxproduct=float("-inf")
        # n=len(nums)
        # def product_subarray (i, product):
        #     nonlocal maxproduct
        #     if i==n:
        #         return product

        #     take= product_subarray(i+1 , product* nums[i])
        #     not_take=product_subarray(i+1 , product)

        #     maxproduct= max(maxproduct, product)
        #     return take*not_take

        # product_subarray(0, 1)
        # return maxproduct

        # p=1
        # maxp=float("-inf")

        # for i in range(len(nums)):
        #     p=p* nums[i]
        #     if p>maxp:
        #         maxp=p

        #     if p<=0:
        #         p=1
        # return maxp

        pref=1
        suff=1

        maxp=float("-inf")

        for i in range(len(nums)):

            if pref==0:
                pref=1
            if suff==0:
                suff=1
            pref=pref* nums[i]
            suff=suff* nums[len(nums)-1-i]

            maxp=max(maxp, max(pref, suff))

        return maxp

            