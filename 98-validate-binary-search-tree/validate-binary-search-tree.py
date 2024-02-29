# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxx, minn = float("inf"), -float("inf")
        def is_valid(cur, minn, maxx):
            if not cur:
                return True
            
            return cur.val > minn and cur.val < maxx and is_valid(cur.left, minn, cur.val) and is_valid(cur.right, cur.val, maxx)
        return is_valid(root, minn, maxx)
            
        