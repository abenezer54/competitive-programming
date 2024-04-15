class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, s):
            nonlocal ans
            if not node.left and not node.right:
                ans += int(s + str(node.val))
            if node.left:
                dfs(node.left, s + str(node.val))
            if node.right:
                dfs(node.right, s + str(node.val))
        ans = 0
        dfs(root, '')
        return ans