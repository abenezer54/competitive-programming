# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                if ans:
                    ans = min(path[::-1], ans)
                else:
                    ans = path[::-1]
            if node.left:
                stack.append((node.left, path + [node.left.val]))
            if node.right:
                stack.append((node.right, path + [node.right.val]))

        res = ''.join([chr(i + 97) for i in ans])
        return res
