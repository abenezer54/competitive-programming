# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([[root, 0]])
        prev = [0, 0]
        while queue:
            node, parity = queue.popleft()

            if parity & 1:
                if node.val & 1:
                    return False
                if prev[1] & 1 and node.val >= prev[0]:
                    return False
            else:
                if not node.val & 1:
                    return False
                if not prev[1] & 1 and node.val <= prev[0]:
                    return False

            prev = [node.val, parity]
            if node.left:
                queue.append([node.left, 1 - parity])
            if node.right:
                queue.append([node.right, 1 - parity])

        return True
