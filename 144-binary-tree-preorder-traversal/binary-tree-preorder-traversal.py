# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(cur):
            if cur:
                ans.append(cur.val)
                dfs(cur.left)
                dfs(cur.right)
        dfs(root)
        return ans
        