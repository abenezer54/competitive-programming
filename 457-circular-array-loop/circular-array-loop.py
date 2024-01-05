class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # O(n) Solution 
        n = len(nums)
        x = 2000
        for i in range(n):
            j = i
            flag = nums[j] > 0
            while True:
                if nums[j] <= 1000:
                    destination = (j + nums[j]) % n
                    nums[j] = x
                    if j == destination:        
                        x += 1
                        break
                    if flag:
                        if nums[destination] < 0:
                            x += 1
                            break
                    else:
                        if nums[destination] > 0:
                            if nums[destination] == x:
                                return True
                            x += 1
                            break
                    
                    j = destination

                else:
                    if nums[j] == x:
                        return True
                    x += 1
                    break

        return False