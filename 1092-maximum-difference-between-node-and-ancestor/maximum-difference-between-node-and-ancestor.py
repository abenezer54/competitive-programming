# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(cur):
            # print(cur.val)
            nonlocal ans
            if not cur:
                return [float('inf'), -float('inf')]
            left = dfs(cur.left)
            right = dfs(cur.right)
            best = [min(left[0], right[0], cur.val), max(left[1], right[1], cur.val)]
            ans = max(ans, abs(cur.val - best[0]), abs(cur.val - best[1]))   
            return best

        dfs(root)
        return ans
