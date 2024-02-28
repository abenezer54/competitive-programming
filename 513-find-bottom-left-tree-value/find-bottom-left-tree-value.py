class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        while queue:
            last = queue.popleft()
            if last.right:
                queue.append(last.right)
            if last.left:
                queue.append(last.left)
        return last.val
        