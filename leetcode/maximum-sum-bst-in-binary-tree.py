# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def max_sum(node):
            nonlocal ans
            if not node:
                return [True, inf, -inf, 0]
  
            l_valid, l_min, l_max, l_sum = max_sum(node.left)
            r_valid, r_min, r_max, r_sum = max_sum(node.right)
            

            cur_valid = node.val > l_max and node.val < r_min and r_valid and l_valid
            cur_max = max(node.val, r_max, l_max)
            cur_min = min(node.val, r_min, l_min)
            cur_sum = r_sum + l_sum + node.val

            if cur_valid:
                ans = max(ans, cur_sum)
                return [True, cur_min, cur_max, cur_sum]
            else:
                return [False, cur_min, cur_max, 0]
        max_sum(root)
        return ans