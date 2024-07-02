type Pair struct {
    Value int
    Index int
}

func twoSum(nums []int, target int) []int {
    pairs := make([]Pair, len(nums))
    for i := 0; i < len(nums); i++ {
        pairs[i] = Pair{nums[i], i}
    }

    sort.Slice(pairs, func(i, j int) bool {
        return pairs[i].Value < pairs[j].Value
    })

    l, r := 0, len(nums)-1
    for l < r {
        sum := pairs[l].Value + pairs[r].Value
        if sum == target {
            return []int{pairs[l].Index, pairs[r].Index}
        } else if sum < target {
            l++
        } else {
            r--
        }
    }

    return []int{}
}
