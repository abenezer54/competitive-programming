class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(arr, k):
            left = 0 
            right = k
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        ans = []
        for i in range(len(arr), 1, -1):
            idx = arr.index(i)
            flip(arr, idx)
            flip(arr, i - 1)
            ans.extend([idx + 1, i])
        
        return ans       
