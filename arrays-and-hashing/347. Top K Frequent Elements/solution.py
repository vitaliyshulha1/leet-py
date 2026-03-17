# 1. Сначала объявляем класс (шаблон с LeetCode)
from typing import List
from collections import Counter


class Solution:
  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    count = Counter(nums) # Counter считает частоты. возваращет Dict.
    return [x for x, _ in count.most_common(k)] # это аналог 
                                                #     result = []
                                                # for x, _ in count.most_common(k):
                                                #     result.append(x)
                                                # return result

# 2. И только в самом конце создаем объект и вызываем метод
sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3,7,7,7,7,7], 2))


#  вначале надо создать Dictionary где ключ цифра, а значение частота с какой число встречается . на пайтоне Counter считает частоты
#  потом сортируем все объекты в Dictionary по значению и возварщаем то количесто которе нужно . most_common(k) воваршает топ К