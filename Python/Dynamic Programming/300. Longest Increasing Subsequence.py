class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        max_ = 1

        for n in range(1, len(nums)):
            for ix in reversed(range(n)):
                if nums[ix] < nums[n]:
                    dp[n] = max(dp[n], dp[ix] + 1)
            max_ = max(max_, dp[n])

        return max_
