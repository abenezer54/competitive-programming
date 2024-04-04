# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, None, None)]
        while stack:
            cur, par, gpar = stack.pop()
            if gpar and gpar.val % 2 == 0:
                ans += cur.val
            if cur.left:
                stack.append((cur.left, cur, par))
            if cur.right:
                stack.append((cur.right, cur, par))
        return ans
        