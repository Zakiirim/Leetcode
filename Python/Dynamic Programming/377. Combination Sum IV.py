class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        
        for x in range(1, target+1):
            dp[x] = 0
            for y in nums:
                dp[x] += dp.get(x-y, 0)

        return dp[target]