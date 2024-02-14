# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        cur = head
        while cur:
            d = dummy
            while d.next and cur.val >= d.next.val:
                d = d.next
            d.next, temp = cur, d.next
            cur = cur.next
            d.next.next = temp
        return dummy.next
        