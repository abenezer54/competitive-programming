func minimumPushes(word string) int {
    cnt := make(map[rune]int)
    for _, ch := range word{
        cnt[ch] += 1
    }
    a := make([]int, 0)
    for _, v := range cnt{
        a = append(a, v)
    }
    slices.Sort(a)
    slices.Reverse(a)

    ans := 0
    for i, v := range a {
        ans += v * ((i / 8) + 1)
    }

    return ans
}