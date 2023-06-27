class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        score = 0
        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif score > 0 and power < tokens[l] and l != r:    
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return score
