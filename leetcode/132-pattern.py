class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n, stack = len(nums), []
        minn = [float('inf')] * n
        for i in range(n):
            if i != 0:
                if minn[i] > nums[i - 1]:
                    minn[i] = nums[i - 1]
                if minn[i] > minn[i - 1]:
                    minn[i] =  minn[i - 1]
                
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if stack:
                if minn[stack[-1]] != float('inf') and  minn[stack[-1]] < nums[i]:
                    return True

            stack.append(i)

        return False
        