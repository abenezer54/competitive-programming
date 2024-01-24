class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = ListNode()
        cur1 = list1
        cur2 = list2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                if not head.next:
                    head.next = cur1
                    tail.next = cur1
                else:
                    tail.next.next = cur1
                    tail.next = cur1
                cur1 = cur1.next
            else:
                if not head.next:
                    head.next = cur2
                    tail.next = cur2
                else:
                    tail.next.next = cur2
                    tail.next = cur2
                cur2 = cur2.next

        while cur1:
            if not head.next:
                head.next = cur1
                tail.next = cur1
            else:
                tail.next.next = cur1
                tail.next = cur1
            cur1 = cur1.next

        while cur2:
            if not head.next:
                head.next = cur2
                tail.next = cur2
            else:
                tail.next.next = cur2
                tail.next = cur2
            cur2 = cur2.next

        return head.next
        