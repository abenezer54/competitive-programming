class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        ptr1, ptr2 = 0, 0
        idx1, idx2 = 0, 0

        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1][idx1] != word2[ptr2][idx2]:
                return False

            idx1 += 1
            idx2 += 1

            if idx1 == len(word1[ptr1]):
                ptr1 += 1
                idx1 = 0

            if idx2 == len(word2[ptr2]):
                ptr2 += 1
                idx2 = 0

        return ptr1 == len(word1) and ptr2 == len(word2)
