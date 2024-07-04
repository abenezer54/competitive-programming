# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        sm = 0
        ans = ListNode()
        dummy = ans
        while cur:
            if cur.val == 0:
                node = ListNode(sm)
                ans.next = node
                ans = ans.next
                sm = 0
            else:
                sm += cur.val
            cur = cur.next
        return dummy.next
