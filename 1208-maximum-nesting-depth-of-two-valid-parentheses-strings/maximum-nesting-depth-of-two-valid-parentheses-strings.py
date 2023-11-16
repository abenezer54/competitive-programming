class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        N = len(seq)
        ans = [0] * N
        
        stackA = []
        stackB = []
        for i, char in enumerate(seq):
            if char == "(":
                if len(stackA) <= len(stackB):
                    stackA.append(char)
                else:
                    stackB.append(char)
                    ans[i] = 1
            else:
                if len(stackA) >= len(stackB):
                    stackA.pop()
                else:
                    stackB.pop()
                    ans[i] = 1
        return ans        