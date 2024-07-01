func reverseString(s []byte)  {
    l, r := 0, len(s) - 1
    for{
        if l >= r{
            break
        }
        temp := s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1
    }
    
}