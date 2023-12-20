class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left_score = [0] * (N + 1)
        right_score = [0] * (N + 1)
        for i in range(N):
            left_score[i + 1] = left_score[i]
            if not nums[i]:
                left_score[i + 1] += 1
                
        for i in range(N - 1, -1, -1):
            right_score[i] = right_score[i + 1]
            if nums[i]:
                right_score[i] +=  1

        total_score = [0] * (N + 1)
        for i in range(N + 1):
            total_score[i] = left_score[i] + right_score[i]

        ans = []
        maximum = max(total_score)
        for i in range(N + 1):
            if total_score[i] == maximum:
                ans.append(i)
         
        return ans
        