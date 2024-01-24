class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast:
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            fast = fast.next
        if slow:
            slow.next = None
        return head
        