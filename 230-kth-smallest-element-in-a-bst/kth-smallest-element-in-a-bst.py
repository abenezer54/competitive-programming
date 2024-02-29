# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(cur):
            if cur:
                dfs(cur.left)
                arr.append(cur.val)
                dfs(cur.right)
        dfs(root)
        return arr[k - 1]
        