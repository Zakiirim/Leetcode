class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0

        for ix in range(1, amount + 1):
            for c in coins:
                if ix - c >= 0:
                    dp[ix] = min(dp[ix], 1 + dp[ix - c])

        return dp[amount] if dp[amount] <= amount else -1
