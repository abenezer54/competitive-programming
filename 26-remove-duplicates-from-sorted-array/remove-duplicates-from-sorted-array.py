class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        holder = 1
        visited = set()
        for seeker in range(1, len(nums)):
            if nums[seeker] not in visited and nums[seeker] != nums[seeker - 1]:
                visited.add(nums[seeker])
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
                
        return holder 
        