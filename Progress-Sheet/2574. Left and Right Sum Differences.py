class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left, right, final =[], [], []
        nums2=nums[::-1]

        for i in range(len(nums)):
            if i==0:
                left.append(0)
                right.append(0)
            else:
                left.append(left[i-1]+nums[i-1])
                right.append(right[i-1]+nums2[i-1])
        right=right[::-1]
        
        for i in range(len(nums)):
            final.append(abs(left[i]-right[i]))
        return final
