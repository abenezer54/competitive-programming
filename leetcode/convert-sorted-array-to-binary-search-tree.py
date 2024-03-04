# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def convert(l, r):
            mid = (r + l) // 2
            if r == l: return TreeNode(nums[l])
            if r < l: return 

            cur_root = TreeNode(nums[mid])
            cur_root.left = convert(l, mid - 1)
            cur_root.right = convert(mid + 1, r)

            return cur_root
        return convert(0, len(nums) - 1)

        