from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Кладём все числа в set — поиск будет за O(1)
        # Дубликаты автоматически удаляются
        num_set = set(nums)

        # Переменная для хранения максимальной длины
        best = 0

        # Перебираем каждое уникальное число из set
        for num in num_set:

            # Ключевая проверка: является ли num началом цепочки?
            # Если num-1 существует в set — значит num не начало, пропускаем.
            # Это и даёт нам O(n): каждое число обрабатываем только один раз
            if num - 1 not in num_set:

                # num — начало цепочки, инициализируем счётчик
                length = 1

                # Идём вправо пока следующее число существует в set
                while num + length in num_set:
                    length += 1  # увеличиваем длину текущей цепочки

                # Обновляем максимум если текущая цепочка длиннее
                best = max(best, length)

        # Возвращаем длину самой длинной найденной цепочки
        return best


# Создаём объект Solution
sol = Solution()

# Тест 1: последовательность 1→2→3→4, длина 4
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4

# Тест 2: последовательность 0→1→2→3, длина 4
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9

# Тест 3: пустой массив
print(sol.longestConsecutive([]))  # 0