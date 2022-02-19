class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = (0, len(height) - 1)
        max_sum = 0

        while l < r:
            max_sum = max(
                max_sum,
                min(height[l], height[r]) * (r - l)
            )
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_sum
