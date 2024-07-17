# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj = defaultdict(list)
        def connect(parent, child):
            if parent and child:
                adj[parent.val].append(child.val)
                adj[child.val].append(parent.val)
            
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)
        connect(None, root)

        que = deque([target.val])
        vis = set([target.val])
        while que:
            if k == 0:
                return list(que) 
            que_len = len(que)
            for _ in range(que_len):
                node = que.popleft()
                for neighbor in adj[node]:
                    if neighbor not in vis:
                        que.append(neighbor)
                        vis.add(neighbor)
            k -= 1
        return []
        