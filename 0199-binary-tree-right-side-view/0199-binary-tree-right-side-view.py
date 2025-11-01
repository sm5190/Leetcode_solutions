# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""Return the values visible from the right side of a binary tree."""
class Solution:
    def rightSideView(self, root: Optional['TreeNode']) -> List[int]:
        ans = []
        def dfs(node, level):
            if not node:
                return
            if level == len(ans):     # first time we reach this depth
                ans.append(node.val)  # right-first ⇒ visible from right
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return ans