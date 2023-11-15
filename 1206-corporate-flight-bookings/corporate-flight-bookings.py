class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n + 2)
        for first, last, seats  in bookings:
            prefix[first] += seats
            prefix[last + 1] -= seats
        for i in range(1, n + 2):
            prefix[i] = prefix[i - 1] + prefix[i]
        
        return prefix[1:-1]
        