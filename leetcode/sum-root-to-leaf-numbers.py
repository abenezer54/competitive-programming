# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def append_char(arr, char):
            if not arr:
                arr.append(char)
                return 
            for i in range(len(arr)):
                arr[i] += char
        
        def dfs(cur):
            if not cur:
                return []
            left = dfs(cur.left)
            right = dfs(cur.right)
            tot = left + right
            append_char(tot, str(cur.val))
            return tot
        ans = dfs(root)

        return sum([int(val[::-1]) for val in ans])
