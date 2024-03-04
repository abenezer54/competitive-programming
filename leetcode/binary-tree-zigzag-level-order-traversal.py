# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        def preorder(cur, depth):
            if not cur:
                return 0
            hashmap[depth].append(cur.val)
            preorder(cur.left, depth + 1)
            preorder(cur.right, depth + 1)
        preorder(root, 0)

        return [arr if not depth & 1 else arr[::-1] for depth, arr in hashmap.items() ]
        