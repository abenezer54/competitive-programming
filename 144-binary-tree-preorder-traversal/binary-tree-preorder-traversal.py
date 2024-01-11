# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        ans = []
        stack = []
        while head:
            ans.append(head.val)
            if head.right:
                stack.append(head.right)
            if head.left:
                head = head.left  
            else:
                if stack:
                    head = stack.pop()
                else:
                    break
            
        return ans
        