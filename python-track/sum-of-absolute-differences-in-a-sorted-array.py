class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix, right, left = [0] * n, [0] * n, [0] * n, [0] * n

        for i in range(1, n):
            right[i] =  nums[i] - nums[i - 1]
            prefix[i] = prefix[i - 1] + right[i]
            
        for i in range(n - 2, -1, -1):
            left[i] =  nums[i + 1] - nums[i]
            suffix[i] = suffix[i + 1] + left[i]

        left.pop()
        left.insert(0, 0)
        cur_left = [0] * n
        left_total = sum(suffix)
        for i in range(n - 1, -1, -1):
            cur_left[i] = left_total
            left_total -= left[i] * i
        
        right_total = sum(prefix)
        ans = [0] * n
        for i in range(n):
            right_total -= right[i] * (n - i)
            ans[i] = right_total + cur_left[i]
            
        return ans
