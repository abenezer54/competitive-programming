# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        td = set(to_delete)
        ans = []
        def dfs(cur, hr):
            if cur:
                if cur.val in td:
                    dfs(cur.left, False)
                    dfs(cur.right, False)
                    return None
                else:
                    left = dfs(cur.left, True)
                    right = dfs(cur.right, True)
                    cur.left = left
                    cur.right = right
                    if hr:
                        return cur
                    else:
                        ans.append(cur)
        dfs(root, False)
        return ans
