# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
                
        def is_leaf(node):
            if not node.left and not node.right:
                return node
        
        res = []
        if not is_leaf(root):
            res.append(root.val)

        # 1) Left boundary (exclude leaves)
        cur = root.left
        while cur:
            if not is_leaf(cur):
                res.append(cur.val)
            cur = cur.left if cur.left else cur.right

        # 2) Leaves (DFS)
        def add_leaves(node):
            if not node:
                return
            if is_leaf(node):
                res.append(node.val)
                return
            add_leaves(node.left)
            add_leaves(node.right)

        add_leaves(root)

        # 3) Right boundary (exclude leaves, then reverse)
        stack = []
        cur = root.right
        while cur:
            if not is_leaf(cur):
                stack.append(cur.val)
            cur = cur.right if cur.right else cur.left
        res.extend(reversed(stack))

        return res

                