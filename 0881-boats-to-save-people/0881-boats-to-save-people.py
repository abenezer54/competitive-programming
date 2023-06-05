class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        onlyOnePerson = people.count(limit)
        count += onlyOnePerson
        arr = list(filter(lambda x : x != limit, people))
        l = 0
        r = len(arr) - 1
        while l <= r:
            if arr[l] + arr[r] <= limit and l != r:
                count += 1
                l += 1
                r -= 1
            elif l == r:
                count += 1
                break
            else:
                count += 1
                r -= 1
        return count