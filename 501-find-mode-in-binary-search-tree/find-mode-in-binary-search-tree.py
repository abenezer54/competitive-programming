# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        maxx = 0
        count = Counter()
        ans = []
        def dfs(cur):
            nonlocal maxx
            if cur:
                count[cur.val] += 1
                if count[cur.val] > maxx:
                    ans.clear()
                    ans.append(cur.val)
                    maxx = count[cur.val]
                elif count[cur.val] == maxx:
                    ans.append(cur.val)
                dfs(cur.left)
                dfs(cur.right)
        dfs(root)
        return ans
        