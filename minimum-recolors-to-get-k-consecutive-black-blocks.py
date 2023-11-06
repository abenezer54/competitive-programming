class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        left = 0
        min_count = float("inf")
        count = 0
        for right in range(N):
            if blocks[right] == "W":
                count += 1
            if right - left + 1 == k:
                min_count = min(min_count, count)
                if blocks[left] == "W":
                    count -= 1
                left += 1
                
        return min_count