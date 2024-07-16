# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        constructed = defaultdict(TreeNode)
        childs = set()
        for parent, child, isLeft in descriptions:
            if parent not in constructed:
                constructed[parent] = TreeNode(parent)
            if child not in constructed:
                constructed[child] = TreeNode(child)

            childs.add(child)
            if isLeft:
                constructed[parent].left = constructed[child]
            else:
                constructed[parent].right = constructed[child]

        for val, node in constructed.items():
            if val not in childs:
                return node