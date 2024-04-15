# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, '')]
        ans = 0
        while stack:
            node, s = stack.pop()

            if not node.right and not node.left:
                ans += int(s + str(node.val))
                
            if node.left:
                stack.append((node.left, s + str(node.val)))
            if node.right:
                stack.append((node.right, s + str(node.val)))

        return ans
        