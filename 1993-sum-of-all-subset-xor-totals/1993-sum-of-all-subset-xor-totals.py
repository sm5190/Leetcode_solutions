class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n=len(nums)
        def subsets(i, total):
            if i==n:
                return total

            take=subsets(i+1, total ^ nums[i])
            not_take= subsets (i+1, total)

            return take + not_take

        ans= subsets(0, 0)
        return ans


            

            