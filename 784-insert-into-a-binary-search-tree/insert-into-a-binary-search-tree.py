# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        def dfs(cur, val):
            if not cur: return TreeNode(val)
        
            if cur.val < val:
                cur.right = dfs(cur.right, val)
            else:
                cur.left = dfs(cur.left, val)
            return cur
        dfs(root, val)
        return root
        