class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        maxx = 0
        while slow and prev:
            maxx = max(maxx, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
            
        return maxx
        