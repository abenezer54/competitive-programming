class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n, stack, look = len(nums), [], defaultdict(int)
        ans = [-1] * n
        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                ans[stack[-1][1]] = num
                stack.pop()
            stack.append([num, i])
        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num:
                ans[stack[-1][1]] = num
                stack.pop()

        return ans
        