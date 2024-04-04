# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, par, gpar):
            nonlocal ans
            if node:
                if gpar and gpar.val % 2 == 0:
                    ans += node.val
                dfs(node.left, node, par)
                dfs(node.right, node, par)
        dfs(root, None, None)
        return ans
        