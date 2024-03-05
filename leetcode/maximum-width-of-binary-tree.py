# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        minmax = defaultdict(lambda: [inf, -inf])
        def dfs(cur, row, col):
            if cur:
                minmax[row][0] = min(minmax[row][0], col)
                minmax[row][1] = max(minmax[row][1], col)
                dfs(cur.left, row + 1, col + col)
                dfs(cur.right, row + 1, col + col + 1)

        dfs(root, 0, 0)
        max_width = 1

        for minn, maxx in minmax.values():
            width = maxx - minn + 1
            max_width = max(max_width, width)

        return max_width
