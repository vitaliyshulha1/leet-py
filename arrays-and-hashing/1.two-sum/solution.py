# 1. Сначала объявляем класс (шаблон с LeetCode)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Твоя логика решения
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return []

# 2. И только в самом конце создаем объект и вызываем метод
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))