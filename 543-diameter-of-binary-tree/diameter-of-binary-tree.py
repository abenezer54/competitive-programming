# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                ans = max(ans, left + right)
                return max(left, right) + 1
            return 0
        dfs(root)
        return ans
        
        