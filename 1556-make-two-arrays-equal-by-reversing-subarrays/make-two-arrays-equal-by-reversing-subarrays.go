func canBeEqual(target []int, arr []int) bool {
    slices.Sort(target)
    slices.Sort(arr)
    for i, v := range target{
        if v != arr[i]{
            return false
        }
    }
    return true
}