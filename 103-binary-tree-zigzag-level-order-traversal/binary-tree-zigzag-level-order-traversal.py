# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans, cur = [], []
        prev, nxt = 1, 0
        direction = 1
        queue = deque([root])
        while queue:
            if direction:
                popped = queue.popleft()
                cur.append(popped.val)
                if popped.left:
                    queue.append(popped.left)
                    nxt += 1
                if popped.right:
                    queue.append(popped.right)
                    nxt += 1
            else:
                popped = queue.pop()
                cur.append(popped.val)
                if popped.right:
                    queue.appendleft(popped.right)
                    nxt += 1
                if popped.left:
                    queue.appendleft(popped.left)
                    nxt += 1
            prev -= 1
            if prev == 0:
                ans.append(cur.copy())
                cur.clear()
                prev = nxt
                nxt = 0
                direction = 1 - direction
        return ans


        