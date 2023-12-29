class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            arr = sorted(list(str(num)), reverse = True)
            queue = deque(arr)
            queue.appendleft(queue.pop())      
            return int("".join(queue))
        else:
            arr = sorted(list(str(num)))
            if arr[0] == "0":
                for i in range(1, len(arr)):
                    if arr[i] != "0":
                        arr[0], arr[i] = arr[i], arr[0]
                        break
            return int("".join(arr))
        return 0
        