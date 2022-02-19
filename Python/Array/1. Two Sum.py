class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        visited[nums[0]] = 0

        for x in range(1, len(nums)):
            if target - nums[x] in visited:
                return [visited[target - nums[x]], x]
            visited[nums[x]] = x
