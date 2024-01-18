class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)
        for first, last, seats in bookings:
            ans[first - 1] += seats
            ans[last] -= seats
        for i in range(1, n + 1):
            ans[i] += ans[i - 1]
        
        return ans[:-1]
        