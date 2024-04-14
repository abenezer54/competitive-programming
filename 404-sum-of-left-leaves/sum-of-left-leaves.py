# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        que = deque([(root, 0)])
        while que:
            node, left = que.popleft()
            if left and not node.left and not node.right:
                ans += node.val
            if node.left:
                que.append((node.left, 1))
            if node.right: 
                que.append((node.right, 0))
        return ans
        
        