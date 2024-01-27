# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = defaultdict(list)
        def dfs(node, h):
            if node is None:
                return 
            dfs(node.left, h + 1)
            level[h].append(node.val)
            dfs(node.right, h + 1)

        dfs(root,0)
        return sum(level[len(level) - 1])