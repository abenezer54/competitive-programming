class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            g = gcd(cur.val, cur.next.val)
            node = ListNode(g, cur.next)
            cur.next = node
            cur = cur.next.next
        return head
        