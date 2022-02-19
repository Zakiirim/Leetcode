class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {numbers[0]: 1}

        for x in range(1, len(numbers)):
            if target - numbers[x] in visited:
                return [visited[target - numbers[x]], x + 1]
            visited[numbers[x]] = x + 1
