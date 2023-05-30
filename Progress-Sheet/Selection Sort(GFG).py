class Solution: 
    def select(self, arr, i):
        mix_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        return arr[min_idx]
        
    def selectionSort(self, arr, n):
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
