# 1. Сначала объявляем класс (шаблон с LeetCode)
from typing import List


class Solution:
   def isAnagram(self, s: str, t: str) -> bool:
        # Твоя логика решения
        return sorted(s) == sorted(t)

# 2. И только в самом конце создаем объект и вызываем метод
sol = Solution()
print(sol.isAnagram("anagram","nagaram"))


