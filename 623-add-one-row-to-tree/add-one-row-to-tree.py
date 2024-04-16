# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root, None)
            return node
        d = 1
        que = deque([root])
        while que:
            l = len(que)
            for _ in range(l):
                cur = que.popleft()
                if d == depth - 1:
                    left = TreeNode(val)
                    right = TreeNode(val)
                    if cur.left:
                        left.left = cur.left
                    if cur.right:
                        right.right = cur.right
                    cur.left = left
                    cur.right = right
                else:
                    if cur.left:
                        que.append(cur.left)
                    if cur.right:
                        que.append(cur.right)
            if d == depth - 1:
                return root
            d += 1
