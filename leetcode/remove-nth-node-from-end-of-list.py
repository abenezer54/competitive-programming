class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = right = head
        prev = dummy
        index = 1
        while right:
            if not right.next:
                prev.next = left.next
                break

            if index >= n:
                prev = left
                left = left.next

            index += 1
            right = right.next

        return dummy.next
        