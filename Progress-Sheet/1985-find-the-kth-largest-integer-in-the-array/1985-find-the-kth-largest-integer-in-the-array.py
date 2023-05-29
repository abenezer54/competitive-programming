class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted(map(int, nums), reverse=True)
        return str(nums[k-1])
    
# With out casting or mapping the strings to integer
        
#         def mycmp(a, b):
#             if len(a) > len(b):
#                 return -1
#             elif len(a) < len(b):
#                 return 1
#             else:
#                 if a > b:
#                     return -1
#                 elif a < b:
#                     return 1
#                 else:
#                     return 0
#         nums.sort(key = cmp_to_key(mycmp))
        
#         return nums[k-1]
