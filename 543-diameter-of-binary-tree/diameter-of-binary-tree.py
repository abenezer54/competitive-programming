class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(cur):
            nonlocal ans
            if not cur:
                return 0
            left = dfs(cur.left)
            right = dfs(cur.right)
            ans = max(ans, left + right)
            return max(left, right) + 1
        dfs(root)
        return ans
