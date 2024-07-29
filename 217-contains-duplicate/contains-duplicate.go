func containsDuplicate(nums []int) bool {
    cnt := make(map[int]int)
    for _, v := range nums{
        cnt[v] += 1
    }
    for _, v := range cnt{
        if v > 1 {
            return true
        }
    }
    return false
}