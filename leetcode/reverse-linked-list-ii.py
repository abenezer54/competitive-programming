# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        position = 0
        l1 = dummy
        l2 = r1 = r2 = None
        flag = False
        while curr:
            position += 1 
            
            if position == left - 1:
                l1 = curr
            if position >= left:
                if position == left:
                    l2 = curr
                nxt = curr.next
                curr.next = prev
                prev = curr
                flag = True

            if position == right:
                
                r1 = curr
                r2 = nxt
                print('ri', r1.next.val)
                break
            if flag:
                curr = nxt
            else:
                curr = curr.next
        if l1:
            print(l1.val, l2.val)
        l1.next = r1
        l2.next = r2
        return dummy.next
        