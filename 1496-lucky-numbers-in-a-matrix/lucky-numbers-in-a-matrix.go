func luckyNumbers (matrix [][]int) []int {
    ans := []int{}
    n, m := len(matrix), len(matrix[0])
    const inff = 1e10
    row, col := make([]int, n), make([]int, m)
    for i := range(row) {
        row[i] = inff
    }

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            row[i] = minInt(row[i], matrix[i][j])
            col[j] = maxInt(col[j], matrix[i][j])
        }
    }
    
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            if matrix[i][j] == row[i] && matrix[i][j] == col[j]{
                ans = append(ans, matrix[i][j])
            }
        }
        }
    return ans
}

func maxInt(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func minInt(a, b int) int {
    if a < b {
        return a
    }
    return b
}