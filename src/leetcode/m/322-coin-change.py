class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [None for _ in range(amount + 1)]
        
        dp[0] = 0
        for coin in coins:
            if coin < len(dp):
                dp[coin] = 1
        
        for i in range(len(dp)):
            
            if dp[i] is None:
                minimum = float("inf")
                for coin in coins:
                    if i - coin < 0 or dp[i - coin] == -1:
                        continue
                    cand = 1 + dp[i - coin]
                    if cand < minimum:
                        minimum = cand
                dp[i] = minimum if minimum != float("inf") else -1
            
            if i == amount:
                return dp[i]
