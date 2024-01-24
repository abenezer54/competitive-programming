class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        nxt = None
        feven = head.next if head else None

        even = None
        odd = head
        i = 0
        while curr and curr.next:
            nxt = curr.next
            curr.next = curr.next.next
            if not i & 1 and curr.next:
                odd = curr.next
            i += 1
            curr = nxt
        if odd:
            odd.next = feven

        return head
        