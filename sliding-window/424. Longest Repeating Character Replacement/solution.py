class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Словарь для хранения частоты каждого символа в текущем окне
        count = {}
        
        # left — левая граница окна, max_f — частота самого частого символа в окне
        left = 0
        max_f = 0
        max_len = 0

        for right in range(len(s)):
            # Увеличиваем частоту текущего символа
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # Обновляем максимум частоты среди всех символов в окне
            max_f = max(max_f, count[s[right]])

            # Если (длина окна - частота самого частого символа) > k,
            # значит нам нужно заменить больше k символов. Окно невалидно.
            while (right - left + 1) - max_f > k:
                # Уменьшаем частоту символа, который выходит из окна, и сдвигаем left
                count[s[left]] -= 1
                left += 1

            # Вычисляем максимальную длину валидного окна
            max_len = max(max_len, right - left + 1)

        return max_len

sol = Solution()

# "XYYX", k = 2 -> Можно заменить оба X на Y или наоборот -> Ответ 4
print(sol.characterReplacement("XYYX", 2))      # 4

# "AAABABB", k = 1 -> Заменяем B на A в середине -> "AAA AA B" -> Ответ 5
print(sol.characterReplacement("AAABABB", 1))   # 5

# "AABABBA", k = 1 -> "AAB AB BA" -> Ответ 4
print(sol.characterReplacement("AABABBA", 1))   # 4

# "" -> пустая строка -> Ответ 0
print(sol.characterReplacement("", 1))          # 0