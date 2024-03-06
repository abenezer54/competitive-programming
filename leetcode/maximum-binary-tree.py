# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        visited = set()
        def construct(l, r):
            if l >= len(nums): return   
            if l == r: 
                if l in visited or r in visited:
                    return 
                visited.add(l)
                return TreeNode(nums[l])

            maxx = max(nums[l: r])

            for i in range(l, r):
                if nums[i] == maxx:
                    idx = i
                    break
            visited.add(idx)
            cur = TreeNode(nums[idx])
            cur.left = construct(l, idx )
            cur.right = construct(idx + 1, r)
            return cur

        return construct(0, len(nums))
 