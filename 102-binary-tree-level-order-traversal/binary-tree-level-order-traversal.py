# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        que = deque([(root, 0)])
        while que:
            cur, d = que.popleft()
            if len(ans) < d + 1:
                ans.append([cur.val])
            else:
                ans[d].append(cur.val)

            if cur.left:
                que.append((cur.left, d + 1))
            if cur.right:
                que.append((cur.right, d + 1))
             
        return ans