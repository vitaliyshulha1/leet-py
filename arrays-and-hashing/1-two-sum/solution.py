class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Этот блок должен быть внутри функции (сдвинут вправо)
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))