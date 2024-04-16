# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 0
        heap = []
        heapify(heap)
        for root in lists:
            if root:
                heappush(heap, (root.val, i, root))
                i += 1
        dummy = ListNode()
        temp = dummy
        while heap:
            val, j, head = heappop(heap)
            temp.next = head
            if head.next:
                heappush(heap, (head.next.val, i, head.next))
                i += 1
            temp = head

        return dummy.next