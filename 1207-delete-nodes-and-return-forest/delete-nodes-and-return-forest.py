# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        stack = [root]
        ans = [root] if root.val not in to_delete else []
        parent = defaultdict(TreeNode)
        while stack:
            cur = stack.pop()
            if cur.right:
                parent[cur.right] = cur
                stack.append(cur.right)
                
            if cur.left:
                parent[cur.left] = cur
                stack.append(cur.left)
                
            if cur.val in to_delete:
                if cur.right and cur.right.val not in to_delete:
                    ans.append(cur.right)

                if cur.left and cur.left.val not in to_delete:
                    ans.append(cur.left)

                if cur in parent:
                    if parent[cur].right == cur:
                        parent[cur].right = None
                    else:
                        parent[cur].left = None    
        
        return ans
        