class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        a = [(nums[i], i) for i in range(len(nums))]
        ans = [0] * len(nums)
        def merge(left, right):
            for num, idx in left:
                ans[idx] += bisect_left(right, num, key=lambda x: x[0])
            return sorted(left + right)  

        def msort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr) //2
            left = msort(arr[:mid])
            right = msort(arr[mid:])
            return merge(left, right)
        msort(a)
        return ans