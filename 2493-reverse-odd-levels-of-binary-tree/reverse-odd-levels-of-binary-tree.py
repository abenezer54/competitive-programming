# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        que = deque([root])
        while que:
            ln = len(que)
            if level & 1:
                for i in range(ln // 2):
                    que[i].val, que[~i].val = que[~i].val, que[i].val
                    
            for _ in range(ln):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            level += 1
        return root

        