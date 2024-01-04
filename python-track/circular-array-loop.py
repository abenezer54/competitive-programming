class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):
            slow = start
            fast = start
            flag = True
            if nums[start] <= 0:
                flag = False
            prev1 = slow
            prev2 = fast
            for _ in range(n):
                slow = (slow + nums[slow]) % n
                fast = (fast + nums[fast]) % n
                prev2 = fast
                if flag:
                    if nums[slow] < 0 or nums[fast]  < 0:
                        break
                else:
                    if nums[slow] > 0 or nums[fast]  > 0:
                        break
                fast = (fast + nums[fast]) % n
                
                # print(slow, fast)
                if flag:
                    if nums[fast]  < 0:
                        break
                else:
                    if nums[fast]  > 0:
                        break
                # print(prev1, prev2)
                if prev1 == slow or prev2 == fast:
                    break
                prev1 = slow
                prev2 = fast
                
                if fast == slow:
                    # print(start, prev2, fast)
                    return True
            # print(start)
        return False

        