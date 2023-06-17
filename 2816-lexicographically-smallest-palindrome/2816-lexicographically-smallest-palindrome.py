class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = [x for x in s]
        
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                if arr[i] < arr[j]:
                    arr[j] = arr[i]
                else:
                    arr[i] = arr[j]
            
            i += 1
            j -= 1
        
        return ''.join(arr)