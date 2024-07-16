# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startPath, destPath, parent = [], [], defaultdict(TreeNode)
        startNode, destNode = None, None

        stack = [root]
        while stack:
            top = stack.pop()
            if top.val == startValue:
                startNode = top
            if top.val == destValue:
                destNode = top

            if top.left:
                parent[top.left] = top
                stack.append(top.left)
            if top.right:
                parent[top.right] = top
                stack.append(top.right)

        cur = startNode
        while cur in parent:
            if parent[cur].left == cur:
                startPath.append("L")
            else:
                startPath.append("R")
            cur = parent[cur]

        cur = destNode
        while cur in parent:
            if parent[cur].left == cur:
                destPath.append("L")
            else:
                destPath.append("R")  
            cur = parent[cur]

        startPath.reverse()
        destPath.reverse()

        i = j = 0
        while i < len(startPath) and j < len(destPath) and startPath[i] == destPath[j]:
            i += 1
            j += 1

        ans = 'U' * (len(startPath) - i) + ''.join(destPath[j:])
        return ans
        