class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr =[]
        for i in nums:
            list1 = list(str(i))
            arr.extend(list1)
        answer = list(map(int, arr))
        return answer