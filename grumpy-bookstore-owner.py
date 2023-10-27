class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        k = minutes
        ans = 0
        current_sum = 0
        max_current_sum = 0
        left = 0
        for right, g in enumerate(grumpy):
            if not g:
                ans += customers[right]
            else:
                current_sum += customers[right]
            if right > k - 2:
                max_current_sum = max(max_current_sum, current_sum)
                if  grumpy[left]:
                    current_sum -= customers[left]
                left += 1
        ans += max_current_sum

        return ans