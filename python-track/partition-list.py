class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        c1 = None
        c2 = dummy
        while c2 and c2.next:
            if not c1 and c2.next.val >= x:
                c1 = c2

            if c1 and c2.next.val < x:
                temp = c2.next
                if c2.next.next:
                    c2.next = c2.next.next
                else:
                    c2.next = None
                
                nxt = c1.next
                c1.next = temp
                temp.next = nxt
                c1 = temp
                # print(c1.val)
            else:
                c2 = c2.next
        return dummy.next
        