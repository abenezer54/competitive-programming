# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        curr = head
        i = 0

        while curr:
            if length & 1:
                if i < length//2:
                    stack.append(curr.val)
                elif i > length // 2:
                    if stack and stack[-1] != curr.val:
                        return False
                    if stack:
                        stack.pop()
            else:
                if i < length//2:
                    stack.append(curr.val)
                else:
                    if stack and stack[-1] != curr.val:
                        return False
                    if stack:
                        stack.pop()
            i += 1
            curr = curr.next

        return True       