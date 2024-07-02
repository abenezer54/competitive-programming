func intersect(nums1 []int, nums2 []int) []int {
    ans := []int{}
    cnt := make(map[int]int)

    for _, num := range nums1 {
        cnt[num]++
    }

    for _, num := range nums2 {
        if cnt[num] > 0 {
            ans = append(ans, num)
            cnt[num]--
        }
    }
    return ans
}
