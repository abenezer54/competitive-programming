class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            l = 0
            r = len(row) -1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1
        for row in image:
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        return image
