class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []

        for num in range(1, target[-1] + 1):
            stack.append("Push")
            if num not in target:
                stack.append("Pop")
                
        return stack