class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        idx = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                idx.append(i)
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            summ = 0
            for j in idx:
                summ += abs(j - i)
            ans[i] = summ
        return ans
        