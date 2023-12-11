class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        parity = [num % 2 == 0 for num in nums]
        previous_sum = 0
        for num in nums:
            if num % 2 == 0:
                previous_sum += num

        ans = []
        for val, idx in queries:
            if parity[idx]:
                previous_sum -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                previous_sum += nums[idx]
                parity[idx] = True
            else:
                parity[idx] = False
            ans.append(previous_sum)
        
        return ans
        