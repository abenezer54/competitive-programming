class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the two initial states 
        # dp[-1] - refers status 1 day ago, dp[-2] refers to status 2 days ago
        # dp[i][0] - represent the profit with having stock in hand
        # dp[i][1] - represent the profit without having stock
        dp = [(-prices[0], 0), (-prices[0], 0)]

        for i in range(1, len(prices)):
            # To have a stock on hand we have two local choices to make. Those are:
            # 1. Keep the previous stock we have
            # 2. Buy new stock. But we can not buy stock if we buy stock yesterday so we check our profit 
            #     without stok two days ago (dp[2][1]) then we buy the current stock( - prices[i]).
            # Finally we can take the maximum of the two choices.
            keep_last_stock = dp[-1][0]
            buy_new_stock = dp[-2][1] - prices[i]
            with_stock = max(keep_last_stock, buy_new_stock)

            # We also have two choices  to continue without having stock. 
            # 1. keep the previous status without stock (dp[-1][1])
            # 2. sell the previous status with stock (dp[-1][0]). Since we can sell at anytime unlike buying
            # we can take yesterdays stock and sell it( + prices[i])
            
            # Take maximum of the two choices
            prev_empty = dp[-1][1]
            sell_previous_stock = dp[-1][0] + prices[i] 
            no_stock = max(prev_empty, sell_previous_stock)
            # Append current day's status with both states
            dp.append((with_stock, no_stock))

        # Finaly we will have our answer taking the maximum from the states having or not having stock at last.
        return max(dp[-1])
        