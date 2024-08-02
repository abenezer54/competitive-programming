func minSwaps(nums []int) int {
    cnt := 0
    for _, v := range nums{
        if v == 1{
            cnt += 1
        }
    }
   

    nums = append(nums, nums...)
    left, cur := 0, 0
    ans := int(1e9)
    for right, val := range nums{
        if val == 0{
            cur += 1
        }
        if right - left + 1 > cnt {
            if nums[left] == 0{
                cur -= 1
            }
            left += 1
        }
        if right - left + 1 == cnt{
            ans = min(ans, cur)
        }     
    }
    return ans
}