class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        
        for x in range(2, len(nums)):
            dp[x] = nums[x] + max(dp[:x-1])
            
        return max(dp[-1], dp[-2])