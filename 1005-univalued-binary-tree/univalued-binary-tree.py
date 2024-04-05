# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        prev = root.val
        que = deque([root])
        while que:
            cur = que.popleft()
            if cur.val != prev:
                return False
            if cur.left:
                que.append(cur.left)
            if cur.right:
                que.append(cur.right)
        return True
        