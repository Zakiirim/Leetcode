class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for ix, val in enumerate(nums):

            if ix > 0 and val == nums[ix - 1]:
                continue

            l, r = (ix + 1, len(nums) - 1)
            while l < r:
                if nums[l] + nums[r] + val == 0:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + val > 0:
                    r -= 1
                else:
                    l += 1
        return res
