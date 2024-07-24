class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        a = [nums1[i] - nums2[i] for i in range(n)]
        ans = 0
        def merge(left, right):     
            nonlocal ans
            right.sort()
            for num in left:
                target = num - diff
                ans += len(right) - bisect_left(right, target)
            return sorted(left + right)

        def msort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) // 2
            left = msort(arr[:mid])
            right = msort(arr[mid:])
            return merge(left, right)

        msort(a)
        return ans
        