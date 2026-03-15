# 1. Сначала объявляем класс (шаблон с LeetCode)
from typing import List


class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
        # Твоя логика решения
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

# 2. И только в самом конце создаем объект и вызываем метод
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))


# seen = [] - список. for num in nums перебирает каждый элемент, получаем вложенный цикл.
# seen = set() хеш таблица . в хеш таблице, каждое число в хеш списке хешируется. результат хэширования — это число (индекс), который указывает,
#  в какой «корзине» (bucket) искать данные внутри выделенного массива памяти. токда компу не надо перебирать все числа, он СРАЗУ чере хеш знает где лежит число. 
# но така таблица не может хранить одинаковые числа