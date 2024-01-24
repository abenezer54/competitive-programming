class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = slow
        if fast:
            right = slow.next

        prev = None
        curr = head
        nxt = None
        while curr != slow:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        while right and prev:
            if right.val != prev.val:
                return False
            right = right.next
            prev = prev.next

        return True
        