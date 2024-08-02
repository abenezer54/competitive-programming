/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func countPairs(root *TreeNode, distance int) int {
    ans := 0

    var dfs func(cur *TreeNode) []int
    dfs = func(cur *TreeNode) []int {
        if cur.Left == nil && cur.Right == nil {
            return []int{1}
        }

        var left, right []int
        if cur.Left != nil {
            left = dfs(cur.Left)
        } else {
            left = make([]int, 0)
        }

        if cur.Right != nil {
            right = dfs(cur.Right)
        } else {
            right = make([]int, 0)
        }

        for _, v1 := range left {
            for _, v2 := range right {
                if v1 + v2 <= distance {
                    ans++
                }
            }
        }

        left = append(left, right...)
        for i := range left {
            left[i]++
        }
        return left
    }

    dfs(root)
    return ans
}
