class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        
        for x in range(1, len(nums)):
            for y in reversed(range(x)):
                if nums[y] >= x - y and dp[y] == 1:
                    dp[x] = 1
                    break
                    
        return dp[-1] == 1