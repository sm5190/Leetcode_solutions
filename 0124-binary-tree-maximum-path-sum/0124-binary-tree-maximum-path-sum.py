# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # maxVal=[0]*1
        maxVal= float("-inf")
        
        def maxpathDown(node):
            nonlocal maxVal
            if not node:
                return 0
            left=max(0, maxpathDown(node.left))
            right=max(0, maxpathDown(node.right))

            maxVal=max(maxVal,left+right+node.val)

            return node.val+max(left,right)

        maxpathDown(root)
        return maxVal
        