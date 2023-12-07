class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = list()
        spaces = set(spaces)
        for i in range(len(s)):
          if i in spaces:
            arr.append(" ")
          arr.append(s[i])

        return "".join(arr)
        