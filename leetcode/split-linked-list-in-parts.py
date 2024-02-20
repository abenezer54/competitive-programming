class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, cur = 0, head
        while cur:
            n += 1
            cur = cur.next
        d = n // k
        z, r = d + 1, n % k
        cur, count, ans = head, 0, []
        while cur:
            if not count:
                ans.append(cur)
            count += 1
            nxt = cur.next
            if r:
                if count == z:
                    cur.next = None
                    r -= 1
                    count = 0
            else:
                if count == d:
                    cur.next = None  
                    count = 0                 
            cur = nxt

        while n < k:
            ans.append(None)
            n += 1
        return ans
              