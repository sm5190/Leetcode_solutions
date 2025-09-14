class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmaps = {}

        for i in range(len(nums)):  
            if target-nums[i] in hashmaps:
                return [i,hashmaps[target-nums[i]]]
            else:
                hashmaps[nums[i]]=i
            
            
                