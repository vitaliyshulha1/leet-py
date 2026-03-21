# 1. Сначала объявляем класс (шаблон с LeetCode)
from typing import List
from collections import Counter


class Solution:
  def productExceptSelf(self, nums: list[int]) -> list[int]:
    n = len(nums)
    answer = [1] * n

    # проход слева: заполняем префиксы
    prefix = 1 # всегда начинаем с 1 потому что леее нулевого эдемента ничего нет
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    # проход справа: умножаем на суффиксы
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# 2. И только в самом конце создаем объект и вызываем метод
sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]


# Шаг 1 — заполни массив prefix:
# prefix[0] = 1          # левее первого элемента ничего нет
# prefix[i] = prefix[i-1] * nums[i-1]

# Шаг 2 — иди справа налево, накапливай суффикс в переменной suffix и сразу умножай на answer[i]:
# suffix = 1
# answer[i] *= suffix
# suffix *= nums[i]