# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical = defaultdict(list)
        def dfs(cur, row, col):
            if cur: 
                vertical[col].append([cur.val, row])
                dfs(cur.left, row + 1, col - 1)
                dfs(cur.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        vertical = dict(sorted(vertical.items()))
        ans = []
        for key, val in vertical.items():
            vertical[key] = sorted(val, key= lambda item: (item[1], item[0]))
            sub = []
            for pair in vertical[key]:
                sub.append(pair[0])
            ans.append(sub)
        return ans
        