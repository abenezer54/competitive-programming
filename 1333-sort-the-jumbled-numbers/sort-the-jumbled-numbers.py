class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = [int(''.join([str(mapping[int(num)]) for num in list(str(num))])) for num in nums]
        mp1 = {nums[i]:arr[i] for i in range(len(nums))}
        mp2 = {nums[i]:i for i in range(len(nums))}
        nums.sort(key=lambda x: (mp1[x], mp2[x]))
        return nums