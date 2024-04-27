# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = deque([root])
        ans = []
        while que:
            l = len(que)
            level_sum = 0
            for _ in range(l):
                node = que.popleft()
                level_sum += node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            ans.append(level_sum / l)
        return ans
        