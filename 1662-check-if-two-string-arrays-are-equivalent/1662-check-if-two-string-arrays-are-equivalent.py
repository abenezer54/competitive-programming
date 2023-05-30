class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        len1, len2 = len(word1), len(word2)
        idx1, idx2 = 0, 0
        char_idx1, char_idx2 = 0, 0

        while idx1 < len1 and idx2 < len2:
            if word1[idx1][char_idx1] != word2[idx2][char_idx2]:
                return False

            char_idx1 += 1
            char_idx2 += 1

            if char_idx1 == len(word1[idx1]):
                idx1 += 1
                char_idx1 = 0

            if char_idx2 == len(word2[idx2]):
                idx2 += 1
                char_idx2 = 0

        return idx1 == len1 and idx2 == len2
