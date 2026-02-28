class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hashmap={}
        # for i in range(len(numbers)):
        #     if (target-numbers[i]) in hashmap:
        #         return list([hashmap[(target-numbers[i])]+1, i+1])
        #     else:
        #         hashmap[numbers[i]]=i


        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1