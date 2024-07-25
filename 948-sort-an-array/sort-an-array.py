class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            tot = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    tot.append(left[i])
                    i += 1
                else:
                    tot.append(right[j])
                    j += 1
                    
            tot += left[i:]
            tot += right[j:]
            return tot
    
        def msort(arr):
            if len(arr) == 1:
                return arr
                
            mid = len(arr) // 2
            left = msort(arr[:mid])
            right = msort(arr[mid:])

            return merge(left, right)

        return msort(nums)
        