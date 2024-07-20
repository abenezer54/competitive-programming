# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        def bfs(node):
            nonlocal ans
            if not node.left and not node.right:
                return [1]
            left = bfs(node.left) if node.left else []
            right = bfs(node.right) if node.right else []
            for num1 in left:
                for num2 in right:
                    if num1 + num2 <= distance:
                        ans += 1
            tot = left + right
            return [num + 1 for num in tot]   
        bfs(root)
        return ans        
