class Solution:
    def smallestNumber(self, pattern: str) -> str:
        arr = [str(num) for num in range(1, len(pattern) + 2)]
        i = 0
        while i < len(pattern):
            if pattern[i] == "D":
                end = i
                while end < len(pattern):
                    if pattern[end] == "I":
                        break
                    end += 1
                arr = arr[:i] + arr[i:end+1][::-1] + arr[end + 1:]
                i = end
            i += 1

        return "".join(arr)
        