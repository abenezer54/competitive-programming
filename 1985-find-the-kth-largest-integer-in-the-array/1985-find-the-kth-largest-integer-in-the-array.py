from functools import cmp_to_key
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def mycmp(a, b):
            if int(a) > int(b):
                return -1
            elif int(a) < int(b):
                return 1
            else:
                return 0
        nums.sort(key = cmp_to_key(mycmp))
        
        return nums[k-1]