class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        look, stack = defaultdict(int), []
        for num in nums2:
            while stack and num > stack[-1]:
                look[stack[-1]] = num
                stack.pop()
            stack.append(num)
            
        for num in stack:
            look[num] = -1

        return [look[num] for num in nums1]