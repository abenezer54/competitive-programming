# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = -1
        count = 0
        def dfs(cur):
            nonlocal ans
            nonlocal count
            if cur:
                dfs(cur.left)
                count += 1
                if count == k:
                    ans = cur.val
                dfs(cur.right)
        dfs(root)
        return ans
        